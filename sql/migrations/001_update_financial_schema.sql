BEGIN;

DROP TABLE IF EXISTS income_statements;
DROP TABLE IF EXISTS balance_sheets;
DROP TABLE IF EXISTS cash_flows;
DROP TABLE IF EXISTS shareholding;


CREATE TABLE income_statements (
    id BIGSERIAL PRIMARY KEY,
    company_id BIGINT NOT NULL REFERENCES companies(id),
    period DATE NOT NULL,
    period_type TEXT NOT NULL,
    statement_type TEXT NOT NULL,
    units_in TEXT NOT NULL,

    revenue NUMERIC,
    other_income NUMERIC,
    total_revenue NUMERIC,
    total_expenses NUMERIC,
    profit_before_tax NUMERIC,
    tax NUMERIC,
    profit_after_tax NUMERIC,
    eps_basic NUMERIC,
    eps_diluted NUMERIC,

    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(
        company_id,
        period,
        period_type,
        statement_type
    )
);


CREATE TABLE balance_sheets (
    id BIGSERIAL PRIMARY KEY,
    company_id BIGINT NOT NULL REFERENCES companies(id),
    period DATE NOT NULL,
    period_type TEXT NOT NULL,
    statement_type TEXT NOT NULL,
    units_in TEXT NOT NULL,

    non_current_assets NUMERIC,
    current_assets NUMERIC,
    total_assets NUMERIC,
    current_liabilities NUMERIC,
    net_current_asset NUMERIC,
    non_current_liabilities NUMERIC,
    equity_capital NUMERIC,
    total_equity_and_liabilities NUMERIC,

    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(
        company_id,
        period,
        period_type,
        statement_type
    )
);


CREATE TABLE cash_flows (
    id BIGSERIAL PRIMARY KEY,
    company_id BIGINT NOT NULL REFERENCES companies(id),
    period DATE NOT NULL,
    period_type TEXT NOT NULL,
    statement_type TEXT NOT NULL,
    units_in TEXT NOT NULL,

    profit_before_tax NUMERIC,
    income_before_wc_changes NUMERIC,
    change_in_assets NUMERIC,
    change_in_liabilities NUMERIC,
    change_in_wc NUMERIC,
    operating_cash_flow NUMERIC,
    investing_cash_flow NUMERIC,
    financing_cash_flow NUMERIC,
    total_cash_flow NUMERIC,
    cash_start_of_year NUMERIC,
    cash_end_of_year NUMERIC,

    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(
        company_id,
        period,
        period_type,
        statement_type
    )
);


CREATE TABLE shareholding (
    id BIGSERIAL PRIMARY KEY,
    company_id BIGINT NOT NULL REFERENCES companies(id),
    period DATE NOT NULL,
    category TEXT NOT NULL,
    percentage NUMERIC NOT NULL,

    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(company_id, period, category)
);

COMMIT;