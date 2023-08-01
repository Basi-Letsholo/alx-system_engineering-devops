#!/usr/bin/env ruby

input = ARGV[0]
pattern = /School/

output = input.scan(pattern)
puts output
