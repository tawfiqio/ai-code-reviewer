# 🤖 AI Code Reviewer

A GitHub bot that automatically reviews pull requests using GPT-4 and posts feedback.

## Features
- Comments on new PRs
- Uses OpenAI to analyze diffs
- Easy to deploy via Flask + GitHub Actions

## Setup

1. Clone the repo
2. Create a `.env` with your `OPENAI_API_KEY` and `GITHUB_TOKEN`
3. Deploy `main.py` on a public server
4. Set webhook in your GitHub repo to point to `/webhook`
5. Add `REVIEW_WEBHOOK_URL` secret in GitHub

## License
Contact Mohamed
