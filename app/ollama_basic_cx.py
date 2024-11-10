import ollama

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": "me gustaria hacer una torta de chocolate, la receta por favor",
        },
    ],
)
print(response["message"]["content"])