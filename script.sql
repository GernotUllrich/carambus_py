DO $$
DECLARE
    rec RECORD;
BEGIN
    FOR rec IN
        SELECT
            table_name,
            column_name
        FROM
            information_schema.columns
        WHERE
            data_type = 'timestamp without time zone'
            AND datetime_precision = 6
    LOOP
        EXECUTE FORMAT(
            'ALTER TABLE %I.%I ALTER COLUMN %I TYPE timestamp without time zone',
            'public',  -- Replace with schema name if needed
            rec.table_name,
            rec.column_name
        );
    END LOOP;
END $$;

