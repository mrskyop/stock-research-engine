CREATE TABLE IF NOT EXISTS companies (
    id BIGSERIAL PRIMARY KEY,
    symbol TEXT NOT NULL UNIQUE,
    company_name TEXT NOT NULL,
    isin TEXT UNIQUE,
    exchange TEXT,
    sector TEXT,
    industry TEXT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS prices_daily (
    id BIGSERIAL PRIMARY KEY,
    company_id BIGINT NOT NULL REFERENCES companies(id),
    trade_date DATE NOT NULL,
    open NUMERIC(18,4),
    high NUMERIC(18,4),
    low NUMERIC(18,4),
    close NUMERIC(18,4),
    volume BIGINT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(company_id, trade_date)
);


CREATE TABLE IF NOT EXISTS income_statements (
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


CREATE TABLE IF NOT EXISTS balance_sheets (
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


CREATE TABLE IF NOT EXISTS cash_flows (
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


CREATE TABLE IF NOT EXISTS shareholding (
    id BIGSERIAL PRIMARY KEY,
    company_id BIGINT NOT NULL REFERENCES companies(id),
    period DATE NOT NULL,
    category TEXT NOT NULL,
    percentage NUMERIC NOT NULL,

    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(company_id, period, category)
);

CREATE TABLE IF NOT EXISTS securities (
    id BIGSERIAL PRIMARY KEY,
    company_id BIGINT NOT NULL REFERENCES companies(id),
    exchange TEXT NOT NULL,
    instrument_key TEXT NOT NULL UNIQUE,
    symbol TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(company_id, exchange)
);
CREATE TABLE IF NOT EXISTS pipeline_runs (
    run_id BIGSERIAL PRIMARY KEY,
    started_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    finished_at TIMESTAMPTZ,
    status TEXT NOT NULL,
    total_securities INTEGER DEFAULT 0,
    successful INTEGER DEFAULT 0,
    failed INTEGER DEFAULT 0,
    records_loaded INTEGER DEFAULT 0
);


CREATE TABLE IF NOT EXISTS pipeline_run_items (
    run_id BIGINT NOT NULL REFERENCES pipeline_runs(run_id),
    company_id BIGINT NOT NULL REFERENCES companies(id),
    symbol TEXT NOT NULL,
    started_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    finished_at TIMESTAMPTZ,
    status TEXT NOT NULL,
    records_loaded INTEGER DEFAULT 0,
    error_message TEXT,

    PRIMARY KEY (run_id, company_id)
);

CREATE TABLE IF NOT EXISTS key_ratios (
    id BIGSERIAL PRIMARY KEY,
    company_id BIGINT NOT NULL REFERENCES companies(id),
    as_of_date DATE NOT NULL,
    ratio_name TEXT NOT NULL,
    company_value NUMERIC,
    sector_value NUMERIC,

    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(company_id, as_of_date, ratio_name)
);
