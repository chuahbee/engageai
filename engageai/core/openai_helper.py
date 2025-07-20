import os
import httpx
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENAI_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")

def get_ai_response(prompt: str) -> str:
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "HTTP-Referer": "http://localhost:8000",  # 或你部署的网站
            "X-Title": "EngageAI",  # 自定义项目名称
        }

        payload = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "你是一个有礼貌的客服助手"},
                {"role": "user", "content": prompt},
            ]
        }

        response = httpx.post(
            f"{OPENROUTER_BASE_URL}/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
        else:
            return f"⚠️ 出错：Error code: {response.status_code} - {response.text}"

    except Exception as e:
        return f"⚠️ 出错：{str(e)}"
