import logging

from app.ingestion.incremental_prices import ingest_prices
from app.ingestion.pipeline import (
    complete_pipeline_run,
    complete_pipeline_run_item,
    create_pipeline_run,
    create_pipeline_run_item,
)
from app.ingestion.prices import get_all_securities
from app.logging_config import configure_logging


logger = logging.getLogger(__name__)


def main():
    configure_logging()

    securities = get_all_securities()

    logger.info(
        "Starting price ingestion for %s securities",
        len(securities),
    )

    run_id = create_pipeline_run(
        total_securities=len(securities)
    )

    successful = 0
    failed = 0
    total_records_loaded = 0

    for security in securities:
        symbol = security.symbol
        company_id = security.company_id

        create_pipeline_run_item(
            run_id=run_id,
            company_id=company_id,
            symbol=symbol,
        )

        try:
            logger.info(
                "Processing %s",
                symbol,
            )

            records_loaded = ingest_prices(symbol)

            complete_pipeline_run_item(
                run_id=run_id,
                company_id=company_id,
                status="SUCCESS",
                records_loaded=records_loaded,
            )

            successful += 1
            total_records_loaded += records_loaded

        except Exception as error:
            failed += 1

            logger.exception(
                "Failed to process %s",
                symbol,
            )

            complete_pipeline_run_item(
                run_id=run_id,
                company_id=company_id,
                status="FAILED",
                records_loaded=0,
                error_message=str(error),
            )

    if failed == 0:
        run_status = "SUCCESS"
    else:
        run_status = "PARTIAL_SUCCESS"

    complete_pipeline_run(
        run_id=run_id,
        status=run_status,
        successful=successful,
        failed=failed,
        records_loaded=total_records_loaded,
    )

    logger.info(
        "Pipeline finished | run_id=%s | status=%s | "
        "successful=%s | failed=%s | records=%s",
        run_id,
        run_status,
        successful,
        failed,
        total_records_loaded,
    )


if __name__ == "__main__":
    main()