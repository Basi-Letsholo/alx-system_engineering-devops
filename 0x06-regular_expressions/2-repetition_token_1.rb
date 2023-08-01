#!/usr/bin/env ruby

input = ARGV[0]
pattern = /hb?tn/

output = input.scan(pattern)
puts output
