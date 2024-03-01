#!/usr/bin/env ruby

# Get the argument passed to the script
log_entry = ARGV[0]

# Define the regular expression pattern
pattern = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

# Use the regular expression match method
match_result = log_entry.match(pattern)

# Extract the desired information
sender = match_result[1]
receiver = match_result[2]
flags = match_result[3]

# Print the extracted information
puts "#{sender},#{receiver},#{flags}"
