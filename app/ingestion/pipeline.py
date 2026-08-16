from sqlalchemy import text

from app.database import engine


def create_pipeline_run(total_securities: int) -> int:
    query = text("""
        INSERT INTO pipeline_runs (
            status,
            total_securities
        )
        VALUES (
            'RUNNING',
            :total_securities
        )
        RETURNING run_id;
    """)

    with engine.begin() as connection:
        run_id = connection.execute(
            query,
            {"total_securities": total_securities},
        ).scalar_one()

    return run_id


def create_pipeline_run_item(
    run_id: int,
    company_id: int,
    symbol: str,
):
    query = text("""
        INSERT INTO pipeline_run_items (
            run_id,
            company_id,
            symbol,
            status
        )
        VALUES (
            :run_id,
            :company_id,
            :symbol,
            'RUNNING'
        );
    """)

    with engine.begin() as connection:
        connection.execute(
            query,
            {
                "run_id": run_id,
                "company_id": company_id,
                "symbol": symbol,
            },
        )


def complete_pipeline_run_item(
    run_id: int,
    company_id: int,
    status: str,
    records_loaded: int,
    error_message: str | None = None,
):
    query = text("""
        UPDATE pipeline_run_items
        SET
            status = :status,
            records_loaded = :records_loaded,
            error_message = :error_message,
            finished_at = CURRENT_TIMESTAMP
        WHERE run_id = :run_id
          AND company_id = :company_id;
    """)

    with engine.begin() as connection:
        connection.execute(
            query,
            {
                "run_id": run_id,
                "company_id": company_id,
                "status": status,
                "records_loaded": records_loaded,
                "error_message": error_message,
            },
        )


def complete_pipeline_run(
    run_id: int,
    status: str,
    successful: int,
    failed: int,
    records_loaded: int,
):
    query = text("""
        UPDATE pipeline_runs
        SET
            status = :status,
            successful = :successful,
            failed = :failed,
            records_loaded = :records_loaded,
            finished_at = CURRENT_TIMESTAMP
        WHERE run_id = :run_id;
    """)

    with engine.begin() as connection:
        connection.execute(
            query,
            {
                "run_id": run_id,
                "status": status,
                "successful": successful,
                "failed": failed,
                "records_loaded": records_loaded,
            },
        )