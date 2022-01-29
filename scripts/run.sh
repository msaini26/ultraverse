#!/bin/bash

# Open browser
open http://localhost:8000

# Run Docker container
docker run -v $(pwd):/venture-insight -p 8000:8000 --name ultraverse ultraverse.azurecr.io/ultraverse
# -v tag allows sync upon save between folder in local machine to a folder in docker container
# $(pwd) Mac/Linux, %cd% Windows command shell, ${pwd} Windows PowerShell