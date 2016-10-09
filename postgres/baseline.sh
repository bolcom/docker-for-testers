#!/bin/bash -eux

{ gosu postgres postgres --single -jE <<-EOSQL
    CREATE DATABASE testnet;
EOSQL
} && { gosu postgres postgres --single -jE <<-EOSQL
    CREATE TABLE kv (key varchar(100) PRIMARY KEY, value varchar(100));
    INSERT INTO kv VALUES ('provider','testnet on pg');
EOSQL
}