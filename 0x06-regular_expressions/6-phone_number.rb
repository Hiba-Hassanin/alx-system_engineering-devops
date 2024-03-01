#!/usr/bin/env ruby

# Get the argument passed to the script
phone_number = ARGV[0]

# Define the regular expression pattern
pattern = /^\d{10}$/

# Use the regular expression match method
match_result = phone_number.match(pattern)

# Print the match result
puts match_result
