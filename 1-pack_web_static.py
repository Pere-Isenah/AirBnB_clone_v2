#!/usr/bin/env bash

# Install 
if command -v nginx >/dev/null 2>&1; then
    echo "Nginx is installed."
else
    echo "installing Nginx."
    sudo apt-get -y update
    sudo apt-get install -y nginx
fi



# configure nginx to listen on port 80
ufw allow 'Nginx HTTP'

# set paths
data_test_path="/data/web_static/releases/test/"
data_shared_path="/data/web_static/shared/"
data_current_path="/data/web_static/current"

#create a data folder
if [ -e "$data_test_path" ]; then
    echo "$data_test_path exist."
else
    sudo mkdir -p "$data_test_path"
    sudo touch "$data_test_path/index.html"
    

    printf %s "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>" > "$data_test_path/index.html"
fi

if [ -d "$data_shared_path" ]; then
    echo "$data_shared_path exist."
else
    sudo mkdir -p "$data_shared_path"
fi


if [ -L "$data_current_path" ]; then
    sudo rm "$data_current_path"
    sudo mkdir -p "$data_current_path"
    ln -s "$data_test_path/index.html" "$data_current_path" 
else
    sudo mkdir -p "$data_current_path"
    sudo ln -s "$data_test_path/index.html" "$data_current_path" 
fi
sudo chown -R ubuntu:ubuntu /data/

#update nginx configuration
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html;
    }
    location /redirect_me {
        return 301 http://cuberule.com/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart
