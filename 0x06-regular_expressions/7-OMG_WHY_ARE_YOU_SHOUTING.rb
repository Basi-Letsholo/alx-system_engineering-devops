#!/usr/bin/env ruby

input = ARGV[0]
pattern = /([A-Z]{1,})+/

puts input.scan(pattern).join
