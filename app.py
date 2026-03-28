from openai import OpenAI
from utils import read_text_from_file
client = OpenAI()

book_text = read_text_from_file(r"C:\Users\12269\Desktop\openAI_project\book.txt")
response = client.responses.create(
  model="gpt-5",
  input = f"Summarize the book in simple words to a 10 year old kid: {book_text}"

)  

print(response.output_text)