#!/bin/sh
cd ../python/lucas/dbStats/
sqlite3 bancoTideal < ../../../sql/geraGraficos6.sql
sqlite3 bancoTideal < ../../../sql/geraGraficos54.sql
cd ../../../sql/
