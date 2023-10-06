#!/usr/bin/env bash
# Installs Nginx, listening on port 80

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Adding the string
echo 'Holberton School' > /var/www/html/index.nginx-debian.html

# Setting up a custom 404 page message
echo -e "Ceci n'est pas une page" > /var/www/html/error_404.html


echo -e "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
	index index.nginx-debian.html;
    location /hbnb_static {
        alias /data/web_static/current;
		index index.nginx-debian.html;
    }
    location /redirect_me {
        return 301 https://en.wikipedia.org/wiki/Nginx;
    }
	error_page 404 /error_404.html;
	location /404 {
		root /etc/html;
		internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart
