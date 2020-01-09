#!/usr/bin/env bash
#Script that sets up your web servers for the deployment of web_static

apt-get -y update
install -y install nginx
ufw allow 'Ngingx HTTP'
mkdir -p /data/web_static/{releases/test, shared}
cat > /data/web_static/test/index.html << 'EOF'
<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>
EOF
ln -s /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/listen 80 default_server /a location /hbnb_static/ {alias /data/web_static/current/;}' /etc/nginx/sitesavailable/default
service nginx restart
