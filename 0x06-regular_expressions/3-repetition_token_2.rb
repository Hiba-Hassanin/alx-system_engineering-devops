#!/usr/bin/env ruby

# Get the argument passed to the script
text_to_match = ARGV[0]

# Define the regular expression pattern
pattern = /^[a-z]+\d+$/

# Use the regular expression match method
match_result = text_to_match.match(pattern)

# Print the match result
puts match_result
