def find_name_in_json(json_data, target_name):
    if isinstance(json_data, dict):
        if 'name' in json_data and json_data['name'] == target_name:
            return json_data
        for key, value in json_data.items():
            if isinstance(value, (dict, list)):
                result = find_name_in_json(value, target_name)
                if result is not None:
                    return result
    elif isinstance(json_data, list):
        for item in json_data:
            if isinstance(item, (dict, list)):
                result = find_name_in_json(item, target_name)
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
                    "name": "KJS",
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

# 찾고자 하는 이름
target_name = "KJS"
result = find_name_in_json(json_data, target_name)

if result is not None:
    print(f"The data with name '{target_name}' is: {result}")
else:
    print(f"No data found with name '{target_name}'")