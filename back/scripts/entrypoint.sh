# uvicorn main:app --reload --host 0.0.0.0 --port 8000
opentelemetry-instrument --logs_exporter otlp --traces_exporter otlp --metrics_exporter otlp --service_name ${APP_NAME} --exporter_otlp_endpoint ${COLLECTOR} uvicorn main:app --host ${APP_HOST} --port ${APP_PORT}

echo "Starting Aci-API Service with Uvicorn and OpenTelemetry"

# echo "$COLLECTOR"
# echo "$APP_NAME"
# echo "$APP_HOST"
# echo "$APP_PORT"

# echo "$DATABASE_USER"
# echo "$DATABASE_PASS"
# echo "$DATABASE_HOST"
# echo "$DATABASE_PORT"

