# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
"""

import os
from django.conf import settings

NGINX_VHOST_CONF_DIR="/usr/local/etc/nginx/site-enabled/"

domain=""
sentry_url=""
organization=""

VHOST_TEMPLATE = """
server {
        listen       80 ;
        server_name %s;
        index index.html index.htm index.php;
        location / {
        proxy_redirect off ;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header REMOTE-HOST $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        client_max_body_size 50m;
        client_body_buffer_size 256k;
        proxy_connect_timeout 30;
        proxy_send_timeout 30;
        proxy_read_timeout 60;
        proxy_buffer_size 256k;
        proxy_buffers 16 256k;
        proxy_busy_buffers_size 512k;
        proxy_temp_file_write_size 512k;
        proxy_next_upstream error timeout invalid_header http_500 http_503 http_404;
        proxy_max_temp_file_size 512m;

        proxy_pass    <%s>;
    }

        log_format nginx_json '{ "@timestamp": "$time_iso8601", '
                         '"@fields": { '
                         '"remote_addr": "$remote_addr", '
                         '"remote_user": "$remote_user", '
                         '"body_bytes_sent": "$body_bytes_sent", '
                         '"request_time": "$request_time", '
                         '"status": "$status", '
                         '"request": "$request", '
                         '"request_method": "$request_method", '
                         '"http_referrer": "$http_referer", '
                         '"http_user_agent": "$http_user_agent", '
                         '"tenantname": "%s" } }';
        access_log /var/log/nginx/%s.json nginx_json;
}
"""


class VHost:
    @staticmethod
    def addVhostConf(domain, sentry_url, organization):
        vhost_file = os.path.join(NGINX_VHOST_CONF_DIR, organization+".conf")
        if not os.path.isdir(NGINX_VHOST_CONF_DIR):
            os.makedirs(NGINX_VHOST_CONF_DIR)
        with open(vhost_file, "w+") as fd:
            contents = VHOST_TEMPLATE % (domain, sentry_url, organization, organization)
            fd.write(contents)

    @staticmethod
    def reload_nginx():
        os.system("nginx -s reload")


if __name__=="__main__":
    os.system("echo 'hello world'")
    VHost.addVhostConf("wanghe.loginsight.cn", "http://localhost:9000", "wanghe")
    VHost.reload_nginx()