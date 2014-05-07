#!/usr/bin/env ruby

count = Proc.new { [1,2,3,4,5].each do |i| print i end; puts } 
your_proc = lambda { puts "Lurch: 'You rang?'" }
my_proc = proc { puts "Morticia: 'Who was at the door, Lurch?'" }

# What kind of objects did you just create?
puts count.class, your_proc.class, my_proc.class

# Calling all procs count.call your_proc.call my_proc.call
count.call 
your_proc.call 
my_proc.call