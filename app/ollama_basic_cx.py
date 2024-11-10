import ollama

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": "me gustaria hacer embedding? que base de datos vectorial podria usar algo con poco requisitos de hardware?",
        },
    ],
)
print(response["message"]["content"])