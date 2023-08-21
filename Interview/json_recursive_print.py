def kjs(json_data, key):
    if key in json_data:
        return json_data[key]
    for value in json_data.values():
        if isinstance(value, dict):
            result = kjs(value, key)
            if result is not None:
                return result
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    result = kjs(item, key)
                    if result is not None:
                        return result
    return None

# 예시로 사용할 JSON 데이터
json_data = {
    "name": "John Doe",
    "age": 30,
    "children": [
        {
            "name": "Jane Doe",
            "age": 5,
            "children": [
                {
                    "name": "Alice",
                    "age": 2
                },
                {
                    "name": "Bob",
                    "age": 3
                }
            ]
        },
        {
            "name": "Mark",
            "age": 8
        }
    ]
}

# 특정 키에 해당하는 값을 찾는 예시
key = "age"
result = kjs(json_data, key)
if result is not None:
    print(f"The value for key '{key}' is: {result}")
else:
    print(f"No value found for key '{key}'")