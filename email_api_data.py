import requests
from send_email import send_email

topic = "tesla"
api_key = "f7a1fd3758394408bcff59c158bbfd6b"
full_url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&language=en&apiKey={api_key}"

# Makes request and gets all content of full_url as one giant string
request = requests.get(full_url)

# Formats request as dictionary data type
content = request.json()

# Access url's "articles" and puts them in string variable body
body = ""
print(content)
for article in content["articles"][:20]:
    # Checks if "title" and "description" have None value to prevent NoneType error in concatenation
    if (article["title"] is not None) and (article["description"] is not None):
        body = body + "\n" + body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

# Changes text to utf-8 encoding to prevent unicode error
body = body.encode("utf-8")
send_email(message=body)