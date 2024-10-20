
### Requirements:

~~~
## WINDOWS
python -m venv venv
./venv/Script/activate
pip install -r ./requirements.txt

## LINUX
python -m venv venv
source venv/bin/activate
pip install -r ./requirements.txt
~~~

### start app:
```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
or
```
opentelemetry-instrument --logs_exporter otlp --traces_exporter otlp --metrics_exporter otlp --service_name aci_api_service --exporter_otlp_endpoint http://localhost:4317 uvicorn main:app --host localhost --port 8000
```

### Build Image

```bash
docker build -t aci_api:vX.0.0 .
docker run -d --name aci_api_service -e ENVIRONMENT=local -e APP_NAME=aci_api_service -e APP_HOST=0.0.0.0 -e APP_PORT=8000 -e COLLECTOR=172.168.0.0 -p 8000:8000 aci_api:vX.0.0

## Run Container

```