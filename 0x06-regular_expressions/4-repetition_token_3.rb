#!/usr/bin/env ruby

input = ARGV[0]
pattern = /hb(t+)?n/

puts input.scan(pattern)
