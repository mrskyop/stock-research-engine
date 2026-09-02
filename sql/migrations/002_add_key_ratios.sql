BEGIN;

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

COMMIT;