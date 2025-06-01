
def flatten_dict(d, parent_key='', sep='.'):
    items = {}
    for key, value in d.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.update(flatten_dict(value, new_key, sep=sep))
        else:
            items[new_key] = value
    return items

data = {
    "name": "Alice",
    "details": {"age": 25, "address": {"city": "New York", "zip": "10001"}}
}

print(flatten_dict(data))
