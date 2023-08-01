#!/usr/bin/env ruby

input = ARGV[0]
pattern = /hbt{2,5}n/

output = input.scan(pattern)
puts output
