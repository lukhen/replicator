chameleon set_configuration_files
python configure.py
chameleon create_replica_schema --debug
chameleon add_source --config default  --source mysql --debug
chameleon init_replica --config default --source mysql --debug
chameleon start_replica --config default --source mysql
top
