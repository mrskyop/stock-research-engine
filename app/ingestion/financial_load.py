from sqlalchemy import text

from app.database import engine
# creating function to save income statements, balance sheets, cash flows, and shareholding data into the database with conflict resolution. Each function takes a list of dictionaries representing rows of data and executes an SQL INSERT statement with an ON CONFLICT clause to update existing records if they already exist. The functions return the number of rows processed.

def save_income_statements(rows: list[dict]):
    query = text("""
        INSERT INTO income_statements (
            company_id,
            period,
            period_type,
            statement_type,
            units_in,
            revenue,
            other_income,
            total_revenue,
            total_expenses,
            profit_before_tax,
            tax,
            profit_after_tax,
            eps_basic,
            eps_diluted
        )
        VALUES (
            :company_id,
            :period,
            :period_type,
            :statement_type,
            :units_in,
            :revenue,
            :other_income,
            :total_revenue,
            :total_expenses,
            :profit_before_tax,
            :tax,
            :profit_after_tax,
            :eps_basic,
            :eps_diluted
        )
        ON CONFLICT (
            company_id,
            period,
            period_type,
            statement_type
        )
        DO UPDATE SET
            units_in = EXCLUDED.units_in,
            revenue = EXCLUDED.revenue,
            other_income = EXCLUDED.other_income,
            total_revenue = EXCLUDED.total_revenue,
            total_expenses = EXCLUDED.total_expenses,
            profit_before_tax = EXCLUDED.profit_before_tax,
            tax = EXCLUDED.tax,
            profit_after_tax = EXCLUDED.profit_after_tax,
            eps_basic = EXCLUDED.eps_basic,
            eps_diluted = EXCLUDED.eps_diluted,
            updated_at = CURRENT_TIMESTAMP;
    """)

    with engine.begin() as connection:
        connection.execute(query, rows)

    return len(rows)

def save_balance_sheets(rows: list[dict]):
    query = text("""
        INSERT INTO balance_sheets (
            company_id,
            period,
            period_type,
            statement_type,
            units_in,
            non_current_assets,
            current_assets,
            total_assets,
            current_liabilities,
            net_current_asset,
            non_current_liabilities,
            equity_capital,
            total_equity_and_liabilities
        )
        VALUES (
            :company_id,
            :period,
            :period_type,
            :statement_type,
            :units_in,
            :non_current_assets,
            :current_assets,
            :total_assets,
            :current_liabilities,
            :net_current_asset,
            :non_current_liabilities,
            :equity_capital,
            :total_equity_and_liabilities
        )
        ON CONFLICT (
            company_id,
            period,
            period_type,
            statement_type
        )
        DO UPDATE SET
            units_in = EXCLUDED.units_in,
            non_current_assets = EXCLUDED.non_current_assets,
            current_assets = EXCLUDED.current_assets,
            total_assets = EXCLUDED.total_assets,
            current_liabilities = EXCLUDED.current_liabilities,
            net_current_asset = EXCLUDED.net_current_asset,
            non_current_liabilities = EXCLUDED.non_current_liabilities,
            equity_capital = EXCLUDED.equity_capital,
            total_equity_and_liabilities =
                EXCLUDED.total_equity_and_liabilities,
            updated_at = CURRENT_TIMESTAMP;
    """)

    with engine.begin() as connection:
        connection.execute(query, rows)

    return len(rows)

def save_cash_flows(rows: list[dict]):
    query = text("""
        INSERT INTO cash_flows (
            company_id,
            period,
            period_type,
            statement_type,
            units_in,
            profit_before_tax,
            income_before_wc_changes,
            change_in_assets,
            change_in_liabilities,
            change_in_wc,
            operating_cash_flow,
            investing_cash_flow,
            financing_cash_flow,
            total_cash_flow,
            cash_start_of_year,
            cash_end_of_year
        )
        VALUES (
            :company_id,
            :period,
            :period_type,
            :statement_type,
            :units_in,
            :profit_before_tax,
            :income_before_wc_changes,
            :change_in_assets,
            :change_in_liabilities,
            :change_in_wc,
            :operating_cash_flow,
            :investing_cash_flow,
            :financing_cash_flow,
            :total_cash_flow,
            :cash_start_of_year,
            :cash_end_of_year
        )
        ON CONFLICT (
            company_id,
            period,
            period_type,
            statement_type
        )
        DO UPDATE SET
            units_in = EXCLUDED.units_in,
            profit_before_tax = EXCLUDED.profit_before_tax,
            income_before_wc_changes =
                EXCLUDED.income_before_wc_changes,
            change_in_assets = EXCLUDED.change_in_assets,
            change_in_liabilities = EXCLUDED.change_in_liabilities,
            change_in_wc = EXCLUDED.change_in_wc,
            operating_cash_flow = EXCLUDED.operating_cash_flow,
            investing_cash_flow = EXCLUDED.investing_cash_flow,
            financing_cash_flow = EXCLUDED.financing_cash_flow,
            total_cash_flow = EXCLUDED.total_cash_flow,
            cash_start_of_year = EXCLUDED.cash_start_of_year,
            cash_end_of_year = EXCLUDED.cash_end_of_year,
            updated_at = CURRENT_TIMESTAMP;
    """)

    with engine.begin() as connection:
        connection.execute(query, rows)

    return len(rows)

def save_shareholding(rows: list[dict]):
    query = text("""
        INSERT INTO shareholding (
            company_id,
            period,
            category,
            percentage
        )
        VALUES (
            :company_id,
            :period,
            :category,
            :percentage
        )
        ON CONFLICT (
            company_id,
            period,
            category
        )
        DO UPDATE SET
            percentage = EXCLUDED.percentage,
            updated_at = CURRENT_TIMESTAMP;
    """)

    with engine.begin() as connection:
        connection.execute(query, rows)

    return len(rows)
