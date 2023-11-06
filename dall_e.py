import openai

api_key = "YOUR_API_KEY"  # 자신의 API 키로 대체

openai.api_key = api_key

response = openai.Completion.create(
  engine="dall-e",
  prompt="Generate an image of a cat with wings",
  max_tokens=50
)

image_url = response.choices[0].text  # 이미지 URL을 가져옴
print("Generated Image URL:", image_url)