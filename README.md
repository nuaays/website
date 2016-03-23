# author: wanghe 

# django-oauth-toolkit-example  集成进了我们的官网系统  

# INSTALL && RUN

- virtualenv env 
- source env/bin/active 
- pip install -r requirements.txt
- ./upgrade.sh
- website: http://localhost:8000
- register app: http://localhost:8000/o/applications

- settings/base.py 
    - OAUTH_SERVER="http://localhost:8000"