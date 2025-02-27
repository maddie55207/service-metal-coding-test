import requests
from pprint import pprint

endpoint_url = "https://jsonplaceholder.typicode.com/todos"

# 1) ---- Get the 200 most recent TODOs ----
recent_todos_response = requests.get(endpoint_url)

if recent_todos_response.status_code in [200, 204]:
    # in the case that more than 200 todos exist, use only the 200 most recent
    todos = recent_todos_response.json()
    most_recent = sorted(todos, key=lambda x: x["id"], reverse=True)[:200]
    # print neatly, most recent first
    print("200 most recent todos:\n")
    pprint(most_recent)
else:
    print(f"Error {recent_todos_response.status_code}: {recent_todos_response.text}")


# ---- 2) Create a TODO ----
next_id = int(most_recent[0]['id']) + 1
todo = {
    'completed': True,
    'id': next_id,
    'title': 'non diam nisl morbi facilisi habitasse aliquam morbi',
    'userId': 9999
}

create_response = requests.post(endpoint_url, todo)

if(create_response.status_code >= 200): # 201 for successful creation
    print("\nCreated todo:\n")
    print(create_response.text)
else:
    print(f"Error {create_response.status_code}: {create_response.text}")

# ---- 3) Delete a TODO given an id ----
id = 200 # arbitrary number
delete_response = requests.delete(f"{endpoint_url}/{id}")

if(delete_response.status_code in [200, 204]):
    print(f"\nDeleted TODO with id {id}")
else:
    print(f"Error {delete_response.status_code}: {delete_response.text}")
