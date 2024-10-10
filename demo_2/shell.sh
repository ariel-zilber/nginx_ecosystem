#!/bin/bash


CONTAINER_ID=$(docker ps | grep $IMAGE | awk '{print $1}')
docker exec -it    $CONTAINER_ID bash
