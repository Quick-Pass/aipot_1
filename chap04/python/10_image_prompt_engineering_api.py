from openai import OpenAI
client = OpenAI(api_key="API 키 입력")

def generate_image(prompt, size="1024x1024"):
    response = client.images.generate(
        prompt=prompt,
        n=1,
        size=size
    )
    return response.data[0].url

prompt_text = "Landscape under the sunset sky, mysterious and dreamy atmosphere, digital art style"
image_url = generate_image(prompt_text, size='1024x1024')

print("이미지 URL:", image_url)