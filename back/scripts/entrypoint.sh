# uvicorn main:app --reload --host 0.0.0.0 --port 8000
# opentelemetry-instrument --logs_exporter otlp --traces_exporter otlp --metrics_exporter otlp --service_name ${APP_NAME} --exporter_otlp_endpoint ${COLLECTOR} uvicorn main:app --host ${APP_HOST} --port ${APP_PORT}

opentelemetry-instrument --logs_exporter otlp --traces_exporter otlp --metrics_exporter otlp --service_name aci_api_service --exporter_otlp_endpoint http://otel-service.default.svc.cluster.local:4317 uvicorn main:app --host 0.0.0.0 --port 8000

echo "Starting Aci-API Service with Uvicorn and OpenTelemetry"


echo "$APP_NAME"
echo "$APP_HOST"
echo "$APP_PORT"
echo "$OTEL_SERVICE_NAME"
echo "$OTEL_EXPORTER_OTLP_ENDPOINT" 
echo "$OTEL_EXPORTER_OTLP_INSECURE"
echo "$OTEL_LOGS_EXPORTER"
echo "$OTEL_METRICS_EXPORTER"
echo "$OTEL_TRACES_EXPORTER"


