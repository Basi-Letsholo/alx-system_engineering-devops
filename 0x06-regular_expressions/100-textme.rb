#!/usr/bin/env ruby

input = ARGV[0]
pattern = /from:(\S{1,})\].+to:(\S{1,})\].+flags:(\S{1,})\]/

puts input.scan(pattern).join(',')
