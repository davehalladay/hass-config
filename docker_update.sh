#!/bin/bash
# script checks for new ha version and update if present, will stop and start ha

docker pull homeassistant/home-assistant | grep "Image is up to date" || (echo Already up to date. Exiting... && exit 0)

CONTAINER_ID=docker ps -aqf "name=home-assistant"
docker stop home-assistant
docker rm CONTAINER_ID
docker run -d --name="home-assistant" -v ~/home-assistant/hass-config:/config -v /etc/localtime:/etc/localtime:ro --restart=always --net=host homeassistant/home-assistant
