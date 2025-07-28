#!/usr/bin/env python3
"""
Simple script to call Claude Sonnet using Amazon Bedrock.
"""

import os
import sys
from anthropic import AnthropicBedrock


def main():
    # Get message from environment variable or use default
    default_msg = 'Hello, Claude! Please write a short poem about automation.'
    user_message = os.getenv('USER_MESSAGE', default_msg)
    
    # Check for required AWS credentials
    aws_key = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret = os.getenv('AWS_SECRET_ACCESS_KEY')
    
    if not aws_key or not aws_secret:
        print("Error: AWS credentials not found. Please set AWS_ACCESS_KEY_ID "
              "and AWS_SECRET_ACCESS_KEY environment variables.")
        sys.exit(1)
    
    # Initialize the Bedrock client
    # Uses AWS credentials from environment variables
    client = AnthropicBedrock(
        aws_access_key=aws_key,
        aws_secret_key=aws_secret,
    )
    
    try:
        print(f"Sending message to Claude Sonnet: {user_message}")
        print("-" * 50)
        
        # Call Claude Sonnet 4 (latest version)
        message = client.messages.create(
            model="us.anthropic.claude-sonnet-4-20250514-v1:0",
            max_tokens=1000,
            messages=[
                {
                    "role": "user", 
                    "content": user_message
                }
            ]
        )
        
        print("Claude's response:")
        print(message.content[0].text)
        print("-" * 50)
        print("✅ Successfully called Claude Sonnet on Bedrock!")
        
    except Exception as e:
        print(f"❌ Error calling Claude: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main() 