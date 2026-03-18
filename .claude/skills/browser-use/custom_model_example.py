"""
使用火山引擎 Ark 自定义模型的 browser-use 示例
"""

import asyncio
import os
from dotenv import load_dotenv

from browser_use import Agent, Browser
from browser_use.llm.openai.chat import ChatOpenAI

# 加载 .env 文件
load_dotenv()

async def main():
    # 配置自定义 LLM（使用 OpenAI 兼容接口）
    llm = ChatOpenAI(
        model=os.getenv("MODEL_NAME", "ark-code-latest"),
        api_key=os.getenv("ANTHROPIC_API_KEY"),
        base_url=os.getenv("ANTHROPIC_BASE_URL"),
        temperature=0.2,
    )

    # 配置浏览器
    browser = Browser(
        headless=False,  # 设置为 False 可以看到浏览器窗口
    )

    # 创建 Agent
    agent = Agent(
        task="打开百度首页，截取屏幕截图",
        llm=llm,
        browser=browser,
    )

    # 运行 Agent
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
