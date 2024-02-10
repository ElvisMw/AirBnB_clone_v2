#!/bin/bash

# Install Nginx if not already installed
if ! dpkg -l nginx &>/dev/null; then
    apt-get update
    apt-get install -y nginx
fi

# Create necessary directories if they don't exist
mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file
echo -e '<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>' > /data/web_static/releases/test/index.html

# Create or recreate symbolic link
if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi
ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership to ubuntu user and group recursively
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
config_block="location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
if ! grep -qF "$config_block" "$config_file"; then
    sed -i "/server_name _;/a $config_block" "$config_file"
fi

# Restart Nginx
service nginx restart

exit 0
