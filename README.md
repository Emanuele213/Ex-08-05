# training-docker-compose

This is the Docker Compose required for the Python training.


## How to:

```bash
# Start the Docker stack
docker-compose -p python-traning up -d
telnet localhost 5432
# Destroy the Docker stack
docker-compose -p python-traning down
```