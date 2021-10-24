#!/usr/bin/ruby
# ruby sample code.
# process every line in a text file with ruby (version 1).
file='sampleFile.txt'
f = File.open(file, "r")
f.each_line { |line|
  puts line
}
f.close

