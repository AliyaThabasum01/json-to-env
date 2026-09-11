import json


def json_to_env(data):
    config = json.loads(data)

    if not isinstance(config, dict):
        raise ValueError("JSON must contain an object")

    lines = []

    for key, value in config.items():
        key = str(key).upper()
        value = str(value).lower() if isinstance(value, bool) else str(value)

        lines.append(f"{key}={value}")

    return "\n".join(lines)
