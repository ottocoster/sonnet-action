# Claude Sonnet GitHub Action

A GitHub Action that calls Claude Sonnet using Amazon Bedrock with Python and uv.

## Setup

### 1. AWS Prerequisites

- Sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup)
- Configure programmatic access
- Subscribe to Anthropic models in [AWS Console > Bedrock > Model Access](https://console.aws.amazon.com/bedrock/home?region=us-west-2#/modelaccess)

### 2. GitHub Secrets

Add the following secrets to your GitHub repository:

- `AWS_ACCESS_KEY_ID`: Your AWS access key ID
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key

Optionally, add this variable:

- `AWS_REGION`: AWS region (defaults to `us-west-2`)

### 3. Running the Action

The action can be triggered in three ways:

1. **Manual trigger**: Go to Actions tab > "Call Claude Sonnet on Bedrock" > "Run workflow"
   - You can customize the message sent to Claude
2. **Push to main**: Automatically runs when code is pushed to the main branch

3. **Pull request**: Automatically runs when a pull request is created

## Local Development

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) package manager

### Setup

1. Install dependencies:

   ```bash
   uv sync
   ```

2. Set environment variables:

   ```bash
   export AWS_ACCESS_KEY_ID="your-access-key"
   export AWS_SECRET_ACCESS_KEY="your-secret-key"
   export AWS_REGION="us-west-2"
   export USER_MESSAGE="Your custom message to Claude"
   ```

3. Run the script:
   ```bash
   uv run python call_claude.py
   ```

## What This Does

This action sends a message to Claude Sonnet 4 via Amazon Bedrock and prints the response. The script:

- Uses the Anthropic Bedrock SDK for Python
- Authenticates using AWS credentials from environment variables
- Calls the `anthropic.claude-sonnet-4-20250514-v1:0` model
- Handles errors gracefully

## Customization

You can modify `call_claude.py` to:

- Use different Claude models (see [model names](https://docs.anthropic.com/en/api/claude-on-bedrock#api-model-names))
- Adjust `max_tokens` for longer/shorter responses
- Add system prompts or conversation history
- Process the response differently

## Model Options

Available Claude models on Bedrock:

- `anthropic.claude-sonnet-4-20250514-v1:0` (Claude Sonnet 4) - **Used by default**
- `anthropic.claude-3-5-sonnet-20241022-v2:0` (Claude Sonnet 3.5)
- `anthropic.claude-3-5-haiku-20241022-v1:0` (Claude Haiku 3.5)
- `anthropic.claude-3-haiku-20240307-v1:0` (Claude Haiku 3)

## Troubleshooting

- **Authentication errors**: Ensure AWS credentials are correctly set as GitHub secrets
- **Model access errors**: Make sure you've subscribed to Anthropic models in AWS Bedrock console
- **Region errors**: Verify the AWS region supports Anthropic models
