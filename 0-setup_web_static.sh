#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# Ensure the script exits on errors
set -e

# Update and install Nginx
sudo apt update -y
sudo apt install -y nginx

# Create directories with correct permissions
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create index.html file with correct permissions
echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>Nginx server test</p>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership recursively
sudo chown -R ubuntu:ubuntu /data

# Update Nginx configuration
echo -e "\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n" | sudo tee -a /etc/nginx/sites-enabled/default

# Restart Nginx
sudo service nginx restart

# Exit successfully
exit 0
