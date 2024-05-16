curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8093/connectors/ -d '
{"name":"fin-cdc",
"config": {
  "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
  "topic.prefix": "cdc_fin_db",
  "database.user": "postgres",
  "database.dbname": "financial_db",
  "database.hostname": "postgres",
  "database.password": "postgres",
  "name": "fin-cdc",
  "plugin.name": "pgoutput"
}}'