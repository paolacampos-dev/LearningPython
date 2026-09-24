import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text) # converts the json string into Pyton object (list of dict)
# simnplified could be write it as:  todos = response.json()  becauser requests already provides Json parsing
# print(todos[:2]) # [{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}, {'userId': 1, 'id': 2, 'title': 'quis ut nam facilis et officia qui', 'completed': False}]

todos_by_user = {}
for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo["userId"]] += 1
        except KeyError:  # in case the user in not present in the dict
            todos_by_user[todo["userId"]] = 1

# New list of tupples with each tupple containing the person as how many items have they completed on descending order
top_users = sorted(todos_by_user.items(),
                    key=lambda x:x[1],  # sorted using the second element of each tupple
                    reverse=True) # make it descending

# Get the second value in the first tupple of the list, which will represent max number of items completed
max_complete = top_users[0][1]

users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)

print(f"user(s) {max_users} completed {max_complete} TODOs") # import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text) # reading from a string not a file object
print(todos[:2]) # [{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}, {'userId': 1, 'id': 2, 'title': 'quis ut nam facilis et officia qui', 'completed': False}]

todos_by_user = {}
for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo["userId"]] += 1
        except KeyError:  # in case the user in not present in the dict
            todos_by_user[todo["userId"]] = 1

# New list of tupples with each tupple containing the person as how many items have they completed on descending order
top_users = sorted(
                todos_by_user.items(),  # becomes each item a tupple (user, number of completions) based on the userId
                key=lambda x:x[1], # changes the sorting based on the number of TODOs
                reverse=True
            )

# Get the second value in the first tupple of the list, which will represent max number of items completed
max_complete = top_users[0][1] # indexing

users = []
for use, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)

print(f"user(s) {max_users} completed {max_complete} TODOs") # user(s) 5 and 10 completed 12 TODOs

# Create a json file that contains all of the completed TODOs for those users
def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"] in users)
    return is_complete and has_max_count

with open("filtered_data_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2) # [{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}, {'userId': 1, 'id': 2, 'title': 'quis ut nam facilis et officia qui', 'completed': False}]
