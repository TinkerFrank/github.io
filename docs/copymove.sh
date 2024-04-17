#!/bin/bash

# Source directory
source_dir="/home/ubuntu/github.io/docs/build/html"

# Destination directory
destination_dir="/home/ubuntu/github.io/site"

# Copy contents of source directory to destination directory
cp -r $source_dir/* $destination_dir

echo "Contents of $source_dir copied to $destination_dir"

