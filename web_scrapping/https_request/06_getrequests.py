import requests
#from requests.exceptions import HTTPError

# url = "https://api.github.com"
# response = requests.get(url)

# if response:
#     print ("Success")  # 200
# else:
#     print("An error has ocurred")

# status_code
# for url in  ["https://api.github.com", "https://api.github.com/invalid"]:
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f'HTTP error ocurred: {http_err}')
#     except Exception as err:
#         print(f'Other error ocurred: {err}')
#     else:
#         print ('success!') 
        # success!
        # HTTP error ocurred: 404 Client Error: Not Found for url: https://api.github.com/invalid

# body of the response:
url = "https://api.github.com"
response = requests.get(url)   
# print(response.content)  # output in a byte format:
# b'{\n  "current_user_url": "https://api.github.com/user",\n  "current_user_authorizations_html_url": "https://github.com/settings/connections/applications{/client_id}",\n  "authorizations_url": "https://api.github.com/authorizations",\n  "code_search_url": "https://api.github.com/search/code?q={query}{&page,per_page,sort,order}",\n  "commit_search_url": "https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}",\n  "emails_url": "https://api.github.com/user/emails",\n  "emojis_url": "https://api.github.com/emojis",\n  "events_url": "https://api.github.com/events",\n  "feeds_url": "https://api.github.com/feeds",\n  "followers_url": "https://api.github.com/user/followers",\n  "following_url": "https://api.github.com/user/following{/target}",\n  "gists_url": "https://api.github.com/gists{/gist_id}",\n  "hub_url": "https://api.github.com/hub",\n  "issue_search_url": "https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}",\n  "issues_url": "https://api.github.com/issues",\n  "keys_url": "https://api.github.com/user/keys",\n  "label_search_url": "https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}",\n  "notifications_url": "https://api.github.com/notifications",\n  "organization_url": "https://api.github.com/orgs/{org}",\n  "organization_repositories_url": "https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}",\n  "organization_teams_url": "https://api.github.com/orgs/{org}/teams",\n  "public_gists_url": "https://api.github.com/gists/public",\n  "rate_limit_url": "https://api.github.com/rate_limit",\n  "repository_url": "https://api.github.com/repos/{owner}/{repo}",\n  "repository_search_url": "https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}",\n  "current_user_repositories_url": "https://api.github.com/user/repos{?type,page,per_page,sort}",\n  "starred_url": "https://api.github.com/user/starred{/owner}{/repo}",\n  "starred_gists_url": "https://api.github.com/gists/starred",\n  "topic_search_url": "https://api.github.com/search/topics?q={query}{&page,per_page}",\n  "user_url": "https://api.github.com/users/{user}",\n  "user_organizations_url": "https://api.github.com/user/orgs",\n  "user_repositories_url": "https://api.github.com/users/{user}/repos{?type,page,per_page,sort}",\n  "user_search_url": "https://api.github.com/search/users?q={query}{&page,per_page,sort,order}"\n}\n'

#print(response.text) # show in text all the endpoints where we can get more info: (API root api.github.com/plus)
# {
#   "current_user_url": "https://api.github.com/user",
#   "current_user_authorizations_html_url": "https://github.com/settings/connections/applications{/client_id}",
#   "authorizations_url": "https://api.github.com/authorizations",
#   "code_search_url": "https://api.github.com/search/code?q={query}{&page,per_page,sort,order}",
#   "commit_search_url": "https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}",
#   "emails_url": "https://api.github.com/user/emails",
#   "emojis_url": "https://api.github.com/emojis",
#   "events_url": "https://api.github.com/events",
#   "feeds_url": "https://api.github.com/feeds",
#   "followers_url": "https://api.github.com/user/followers",
#   "following_url": "https://api.github.com/user/following{/target}",
#   "gists_url": "https://api.github.com/gists{/gist_id}",
#   "hub_url": "https://api.github.com/hub",
#   "issue_search_url": "https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}",
#   "issues_url": "https://api.github.com/issues",
#   "keys_url": "https://api.github.com/user/keys",
#   "label_search_url": "https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}",
#   "notifications_url": "https://api.github.com/notifications",
#   "organization_url": "https://api.github.com/orgs/{org}",
#   "organization_repositories_url": "https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}",
#   "organization_teams_url": "https://api.github.com/orgs/{org}/teams",
#   "public_gists_url": "https://api.github.com/gists/public",
#   "rate_limit_url": "https://api.github.com/rate_limit",
#   "repository_url": "https://api.github.com/repos/{owner}/{repo}",
#   "repository_search_url": "https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}",
#   "current_user_repositories_url": "https://api.github.com/user/repos{?type,page,per_page,sort}",
#   "starred_url": "https://api.github.com/user/starred{/owner}{/repo}",
#   "starred_gists_url": "https://api.github.com/gists/starred",
#   "topic_search_url": "https://api.github.com/search/topics?q={query}{&page,per_page}",
#   "user_url": "https://api.github.com/users/{user}",
#   "user_organizations_url": "https://api.github.com/user/orgs",
#   "user_repositories_url": "https://api.github.com/users/{user}/repos{?type,page,per_page,sort}",
#   "user_search_url": "https://api.github.com/search/users?q={query}{&page,per_page,sort,order}"
# }

#print(response.json()) # give us back a json dictionary
# {
#   "current_user_url": "https://api.github.com/user",
#   "current_user_authorizations_html_url": "https://github.com/settings/connections/applications{/client_id}",
#   "authorizations_url": "https://api.github.com/authorizations",
#   "code_search_url": "https://api.github.com/search/code?q={query}{&page,per_page,sort,order}",
#   "commit_search_url": "https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}",
#   "emails_url": "https://api.github.com/user/emails",
#   "emojis_url": "https://api.github.com/emojis",
#   "events_url": "https://api.github.com/events",
#   "feeds_url": "https://api.github.com/feeds",
#   "followers_url": "https://api.github.com/user/followers",
#   "following_url": "https://api.github.com/user/following{/target}",
#   "gists_url": "https://api.github.com/gists{/gist_id}",
#   "hub_url": "https://api.github.com/hub",
#   "issue_search_url": "https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}",
#   "issues_url": "https://api.github.com/issues",
#   "keys_url": "https://api.github.com/user/keys",
#   "label_search_url": "https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}",
#   "notifications_url": "https://api.github.com/notifications",
#   "organization_url": "https://api.github.com/orgs/{org}",
#   "organization_repositories_url": "https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}",
#   "organization_teams_url": "https://api.github.com/orgs/{org}/teams",
#   "public_gists_url": "https://api.github.com/gists/public",
#   "rate_limit_url": "https://api.github.com/rate_limit",
#   "repository_url": "https://api.github.com/repos/{owner}/{repo}",
#   "repository_search_url": "https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}",
#   "current_user_repositories_url": "https://api.github.com/user/repos{?type,page,per_page,sort}",
#   "starred_url": "https://api.github.com/user/starred{/owner}{/repo}",
#   "starred_gists_url": "https://api.github.com/gists/starred",
#   "topic_search_url": "https://api.github.com/search/topics?q={query}{&page,per_page}",
#   "user_url": "https://api.github.com/users/{user}",
#   "user_organizations_url": "https://api.github.com/user/orgs",
#   "user_repositories_url": "https://api.github.com/users/{user}/repos{?type,page,per_page,sort}",
#   "user_search_url": "https://api.github.com/search/users?q={query}{&page,per_page,sort,order}"
# }

def print_d(json):
    for key, value in json.items():
        print(f'{key}: {value}')

json_response = response.json()
print_d(json_response)
# current_user_url: https://api.github.com/user
# current_user_authorizations_html_url: https://github.com/settings/connections/applications{/client_id}
# authorizations_url: https://api.github.com/authorizations
# code_search_url: https://api.github.com/search/code?q={query}{&page,per_page,sort,order}
# commit_search_url: https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}
# emails_url: https://api.github.com/user/emails
# emojis_url: https://api.github.com/emojis
# events_url: https://api.github.com/events
# feeds_url: https://api.github.com/feeds
# followers_url: https://api.github.com/user/followers
# following_url: https://api.github.com/user/following{/target}
# gists_url: https://api.github.com/gists{/gist_id}
# hub_url: https://api.github.com/hub
# issue_search_url: https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}
# issues_url: https://api.github.com/issues
# keys_url: https://api.github.com/user/keys
# label_search_url: https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}
# notifications_url: https://api.github.com/notifications
# organization_url: https://api.github.com/orgs/{org}
# organization_repositories_url: https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}
# organization_teams_url: https://api.github.com/orgs/{org}/teams
# public_gists_url: https://api.github.com/gists/public
# rate_limit_url: https://api.github.com/rate_limit
# repository_url: https://api.github.com/repos/{owner}/{repo}
# repository_search_url: https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}
# current_user_repositories_url: https://api.github.com/user/repos{?type,page,per_page,sort}
# starred_url: https://api.github.com/user/starred{/owner}{/repo}
# starred_gists_url: https://api.github.com/gists/starred
# topic_search_url: https://api.github.com/search/topics?q={query}{&page,per_page}
# user_url: https://api.github.com/users/{user}
# user_organizations_url: https://api.github.com/user/orgs
# user_repositories_url: https://api.github.com/users/{user}/repos{?type,page,per_page,sort}
# user_search_url: https://api.github.com/search/users?q={query}{&page,per_page,sort,order}

print(json_response['repository_url']) # https://api.github.com/repos/{owner}/{repo}

print(response.headers) # dict object

# indiferent lower case or capital case
print(response.headers['content-type']) 
print(response.headers['Content-Type']) 
