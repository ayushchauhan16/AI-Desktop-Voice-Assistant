from openai import OpenAI
client = OpenAI(
    api_key="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",)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful virtual assistant name Thor skilled in general task like Alexa and Goggle cloud."},
        {
            "role": "user",
            "content": "What is coding."
        }
    ]
)

print(completion.choices[0].message)