from google import genai
from dotenv import load_dotenv

load_dotenv(override=True)

client = genai.Client()

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = "Explain how AI works in a few words.",
)

print(response.text)