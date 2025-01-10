import requests, os
import google.generativeai as genai
from bs4 import BeautifulSoup

#Parse the text from url
url = input("Input wiki URL > ")

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

#div
#mw-parser-output
#p

print()
print("Summary:")
article = soup.find_all("div", {"class": "mw-parser-output"})[1]

content = article.find_all("p")

text = ""
for p in content:
  text += p.text

#Ask LLM (Gemini) to summarize the text we scrape from wikipedia
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")


prompt = f"Summarise the text below in no more than 3 paragraphs. {text}"

chat = model.start_chat()
response = chat.send_message(prompt)

print(response.text)

#print(response["choices"][0]["text"].strip())


#Getting the reference
refs = soup.find_all("ol", {"class": "references"})
for ref in refs:
  print(ref.text.replace("^ ", ""))