curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8093/connectors/ -d '{
  "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
  "topic.prefix": "cdc_fin_db",
  "database.user": "postgres",
  "database.dbname": "financial_db",
  "database.hostname": "postgres",
  "database.password": "postgres",
  "name": "Postgres",
  "plugin.name": "pgoutput"
}'