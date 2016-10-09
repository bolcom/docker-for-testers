#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE TABLE kv (key varchar(100) PRIMARY KEY, value varchar(100));
    INSERT INTO kv VALUES ('provider','testnet on pg');
EOSQL