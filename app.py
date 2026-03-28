from openai import OpenAI
from utils import read_text_from_file, chunk_text
client = OpenAI()

book_text = read_text_from_file(r"C:\Users\12269\Desktop\openAI_project\book.txt")
chunks = chunk_text(book_text, 100)

print("no.of chunks:" , len(chunks))

#output =[]
for chunk in chunks:
    chunk_summary = client.responses.create(
        model="gpt-5.4",
        input = f"Summarize this text: {chunk}"
    )
    #output.append(chunk_summary)
    print(chunk_summary.output_text, end="==============================")
    


# for i in range(0, len(output)):
#     print("chunk_number:",i+1, "Summary:", output[i], end=" ")    


# response = client.responses.create(
#   model="gpt-5",
#   input = f"Summarize the book in simple words to a 10 year old kid: {book_text}"

# )  

