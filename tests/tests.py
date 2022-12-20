from API import Api

"""
api = Api("https://catfact.ninja/", expectedOutputFormat="text")

res = api.get("fact")

print(res)
"""

api = Api("https://panel.seihost.fr/", expectedOutputFormat="json", baseHeaders={'Authorization': 'Bearer ptla_IIbiKs4IDi5m7JSWAv9NobCNh3JkH9z9wWnXCmE3geI',
  'Accept': 'application/json', 
  'Content-Type': 'application/json'}, controllErrorCode=True, debug=True)

r = api.get('api/application/users')

"""params={
  "email": "example10@example.com",
  "username": "exampleuser",
  "first_name": "Example",
  "last_name": "User"
}"""

print(r)