#!/usr/bin/ruby
# ruby sample code.
# process every line in a text file with ruby (version 1).
file='sampleFile.txt'
File.readlines(file).each do |line|
  puts line
end
