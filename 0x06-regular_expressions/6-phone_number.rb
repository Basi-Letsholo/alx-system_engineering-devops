#!/usr/bin/env ruby

input = ARGV[0]
pattern = /^\d{10}$/

puts input.scan(pattern)
