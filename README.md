# XCAI777 AI API Gateway Quickstart

用一个 OpenAI 风格的 HTTP 接口接入多种 AI 模型，适合把聊天、文本生成和多模态能力接入自己的应用。

- **普通用户**：前往 [XCAI777 AI 聚合平台](https://www.777xcai.com/) 使用 AI 对话、AI 绘画、AI 视频、AI 语音和 AI 智能体。
- **开发者**：前往 [XCAI777 API 网关](https://7777777api.com/) 获取 API Key 和查看模型/接口文档。

## 这个示例能做什么

示例使用 `https://7777777api.com/v1` 作为 API Base URL，通过环境变量读取 API Key，并调用 `/v1/responses` 发送一次文本请求。Python 示例只使用标准库，不需要安装第三方 SDK。你可以把它改成自己的客服、内容生成、知识库问答或自动化工作流。

代码里没有写入任何真实密钥。请把密钥放在本地环境变量中，不要提交到 GitHub。

## 快速开始

```bash
git clone https://github.com/apixc777/xcai777-github-quickstart.git
cd xcai777-github-quickstart
# 需要 Python 3.9+
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate

export XCAI777_API_KEY="替换为你的 API Key"
export XCAI777_MODEL="你的模型名称"
python python_responses.py
```

也可以直接用 curl：

```bash
export XCAI777_API_KEY="替换为你的 API Key"
export XCAI777_MODEL="你的模型名称"
bash curl-responses.sh
```

## 环境变量

| 变量 | 必填 | 说明 |
| --- | --- | --- |
| `XCAI777_API_KEY` | 是 | 在 API 网关控制台创建的密钥 |
| `XCAI777_MODEL` | 是 | 在模型广场或文档中确认的模型名 |
| `XCAI777_BASE_URL` | 否 | 默认是 `https://7777777api.com/v1` |

## 适合的项目

- AI 客服、企业内部问答和知识库助手
- 文章、商品描述、短视频脚本和营销文案生成
- 多模型对比、模型路由和 AI 工作流原型
- 将 AI 对话、图片、视频、语音能力接入网站或 SaaS

## 安全与使用说明

- 不要把 API Key 写入源码、前端代码、截图或公开 issue。
- 生产环境应使用服务端环境变量或密钥管理服务，并设置额度和日志脱敏。
- 模型名称、价格、限额和可用接口以 API 网关当前文档和控制台为准。
- 请遵守上游模型的内容政策、版权要求和适用法律。

## 关键词

`AI API` `API 网关` `AI API 中转站` `OpenAI Compatible API` `多模型聚合` `Gemini API` `Claude API` `GPT API` `DeepSeek API` `Qwen API` `AI 对话` `AI 绘画` `AI 视频` `AI 智能体` `LLM Gateway` `Python HTTP API` `SaaS AI 接入`

## 相关链接

- [XCAI777 聚合平台](https://www.777xcai.com/)
- [XCAI777 API 网关](https://7777777api.com/)
- [API 文档入口](https://7777777api.com/docs-landing.html)
- [模型广场](https://7777777api.com/pricing)
