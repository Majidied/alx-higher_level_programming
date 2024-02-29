#!/bin/bash

# Check if URL is provided as argument
if [ $# -eq 0 ]; then
  echo "Error: URL is missing."
  exit 1
fi

# Send request to the URL and store the response in a variable
response=$(curl -sI "$1")

# Extract the content length from the response headers
content_length=$(echo "$response" | grep -i "content-length:" | awk '{print $2}' | tr -d '\r')

# Check if content length is empty
if [ -z "$content_length" ]; then
  echo "Error: Failed to retrieve content length."
  exit 1
fi

# Display the content length in bytes
echo "Content Length: $content_length bytes"
