import yaml
import os

config = {}

config["pid_dir"] = "~/.pg_chameleon/pid/"
config["log_dir"] = "~/.pg_chameleon/logs/"
config["log_dest"] = "file"
config["log_level"] = "info"
config["log_days_keep"] = 10
config["rollbar_key"] = ""
config["rollbar_env"] = ""

config["type_override"] = {
    "tinyint(1)": {"override_to": "boolean", "override_tables": ["*"]}
}

config["pg_conn"] = {
    "host": os.environ.get("POSTGRES_HOST"),
    "port": "5432",
    "user": os.environ.get("POSTGRES_USER"),
    "password": os.environ.get("POSTGRES_PASSWORD"),
    "database": "pgdb",
    "charset": "utf8",
}

config["sources"] = {
    "mysql": {
        "db_conn": {
            "host": os.environ.get("MYSQL_HOST"),
            "port": "3306",
            "user": os.environ.get("MYSQL_USER"),
            "password": os.environ.get("MYSQL_USER_PASSWORD"),
            "charset": "utf8",
            "connect_timeout": 10,
        },
        "schema_mappings": {
            os.environ.get("MYSQL_DATABASE"): os.environ.get(
                "POSTGRES_DESTINATION_SCHEMA"
            )
        },
        "limit_tables": [
            "{}.{}".format(os.environ.get("MYSQL_DATABASE"), "Users"),
            "{}.{}".format(os.environ.get("MYSQL_DATABASE"), "Klienci"),
            "{}.{}".format(os.environ.get("MYSQL_DATABASE"), "kli_status"),
            "{}.{}".format(os.environ.get("MYSQL_DATABASE"), "Rezerwacje"),
            "{}.{}".format(os.environ.get("MYSQL_DATABASE"), "rez_skad"),
            "{}.{}".format(os.environ.get("MYSQL_DATABASE"), "rez_status"),
            "{}.{}".format(os.environ.get("MYSQL_DATABASE"), "rooms"),
            "{}.{}".format(os.environ.get("MYSQL_DATABASE"), "room_groups"),
            "{}.{}".format(os.environ.get("MYSQL_DATABASE"), "room_group_quantity"),
            "{}.{}".format(os.environ.get("MYSQL_DATABASE"), "room_type_codes"),
            "{}.{}".format(os.environ.get("MYSQL_DATABASE"), "new_ext_rateplans"),
            "{}.{}".format(os.environ.get("MYSQL_DATABASE"), "new_rateplan_periods"),
        ],
        "skip_tables": None,
        "grant_select_to": [os.environ.get("POSTGRES_USER")],
        "lock_timeout": "120s",
        "my_server_id": 100,
        "replica_batch_size": 10000,
        "replay_max_rows": 10000,
        "batch_retention": "1 day",
        "copy_max_memory": "300M",
        "copy_mode": "file",
        "out_dir": "/tmp",
        "sleep_loop": 1,
        "on_error_replay": "continue",
        "on_error_read": "continue",
        "auto_maintenance": "disabled",
        "gtid_enable": "false",
        "type": "mysql",
        "skip_events": {"insert": None, "delete": None, "update": None},
    }
}

# config2 = {}
with open("/home/pg/.pg_chameleon/configuration/default.yml", "w") as conf_file:
    yaml.dump(config, conf_file)


def pr_dct(dct1, dct2, tab):
    for key in dct1.keys():
        if hasattr(dct1[key], "keys"):
            print(tab, key)
            pr_dct(dct1[key], dct2[key], tab + "  ")
        else:
            print(tab, key, dct1[key], dct2[key])
