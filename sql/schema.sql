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
    revenue NUMERIC,
    ebitda NUMERIC,
    ebit NUMERIC,
    profit_after_tax NUMERIC,
    eps NUMERIC,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(company_id, period, period_type)
);


CREATE TABLE IF NOT EXISTS balance_sheets (
    id BIGSERIAL PRIMARY KEY,
    company_id BIGINT NOT NULL REFERENCES companies(id),
    period DATE NOT NULL,
    period_type TEXT NOT NULL,
    total_assets NUMERIC,
    total_liabilities NUMERIC,
    equity NUMERIC,
    total_debt NUMERIC,
    cash NUMERIC,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(company_id, period, period_type)
);


CREATE TABLE IF NOT EXISTS cash_flows (
    id BIGSERIAL PRIMARY KEY,
    company_id BIGINT NOT NULL REFERENCES companies(id),
    period DATE NOT NULL,
    period_type TEXT NOT NULL,
    operating_cash_flow NUMERIC,
    investing_cash_flow NUMERIC,
    financing_cash_flow NUMERIC,
    capital_expenditure NUMERIC,
    free_cash_flow NUMERIC,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(company_id, period, period_type)
);


CREATE TABLE IF NOT EXISTS shareholding (
    id BIGSERIAL PRIMARY KEY,
    company_id BIGINT NOT NULL REFERENCES companies(id),
    period DATE NOT NULL,
    promoter NUMERIC,
    fii NUMERIC,
    dii NUMERIC,
    public_holding NUMERIC,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(company_id, period)
);