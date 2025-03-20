#!/bin/bash

echo "Waiting for Flask app to start..."
sleep 5  # Wait for the container to start

response=$(curl -s "http://localhost:5000/add?num1=5&num2=3")

if [ "$response" == "8.0" ]; then
    echo "Test Passed!"
    exit 0
else
    echo "Test Failed!"
    exit 1
fi
