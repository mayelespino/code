#!/usr/bin/ruby
# 
#
class Song
  def initialize(name, artist, duration)
    @name     = name
    @artist   = artist
    @duration = duration
  end
  def to_s
    "Song: #{@name}--#{@artist} (#{@duration})"
  end

end

aSong = Song.new("lala","blabla",4.5)
bSong = Song.new("bbb","BBBB",5)

puts aSong.to_s()
