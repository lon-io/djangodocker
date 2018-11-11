#!/usr/bin/env bash

echo "Starting container ..."
docker-compose -p djangodocker up -d

# Exec the bash command on the container to attach to STDIN
echo "Attaching to container ..."
docker exec -it djangodocker_web sh -c "bash"

# Clean up after exiting from bash
echo "Cleaning up ..."
docker-compose -p djangodocker down
