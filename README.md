## This repo is an [Ansible AWX](https://github.com/ansible/awx.git) fork.

#### Before installing set variables in the file:
- awx/installer/inventory
```shell
[all:vars]
dockerhub_base=ansible
awx_task_hostname=awx
awx_web_hostname=awxweb
postgres_data_dir="/home/ubuntu/pgdocker"
host_port=80
host_port_ssl=443
docker_compose_dir="/home/ubuntu/awx"
pg_username=awx
pg_password=brown
pg_database=awx
pg_port=5432
admin_user=userawx
admin_password=password
create_preload_data=True
secret_key=0ff1be9a52df0acad86e4461872b88b49e9fe260ee2dcbe33ce078e17f61f2f7
project_data_dir=/home/ubuntu/projects
```