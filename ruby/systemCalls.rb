#!/usr/bin/ruby

puts "Using the system command."

system "ls"

puts "Using the shell command"
puts "output: " + `ls`
