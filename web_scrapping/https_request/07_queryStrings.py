import requests

url = "https://api.github.com/search/repositories"

response = requests.get(
    url, 
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

json_response = response.json()
repository = json_response['items'] [0]
print(f'Text matches: {repository["text_matches"]}')
print(f'Repository name: {repository["description"]}')
# Text matches: [{'object_url': 'https://api.github.com/repositories/33210074', 'object_type': 'Repository', 'property': 'description', 'fragment': 'Set of Python scripts to perform SecRules language evaluation on a given http request.', 'matches': [{'text': 'Python', 'indices': [7, 13]}, {'text': 'language', 'indices': [42, 50]}, {'text': 'request', 'indices': [78, 85]}]}]
# Repository name: Set of Python scripts to perform SecRules language evaluation on a given http request.
