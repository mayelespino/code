#!/usr/bin/ruby
puts "--1--"
puts 'Python language'
puts "Ruby language"
puts "There are many stars" 
puts "He said, \"Which one is your favourite?\""

puts "--2--"
puts 'There are many stars'
puts 'He said, "Which one is your favourite?"'
puts "one two three four"
puts "one\ntwo\nthree\nfour"

puts "--3--"
puts "   bbb\raaa" 
puts "Joan\b\b\bane" 
puts "Towering\tinferno" 
puts "The special character \\"
puts "The special character \'"
puts "The special character \""

puts "--4--"
msg = "Ruby language"
puts msg["Ruby"]
puts msg["Python"]
puts msg[0]
puts msg[-1]
puts msg[0, 3]
puts msg[0..9]
puts msg[0, msg.length]

puts "--5--"
puts "I hear Mariachi static on my radio 
And the tubes they glow in the dark 
And I'm there with her in Ensenada 
And I'm here in Echo Park
"

puts %/
Carmelita hold me tighter
I think I'm sinking down 
And I'm all strung out on heroin
On the outskirts of town/

puts <<STRING

Well, I'm sittin' here playing solitaire
With my pearl-handled deck 
The county won't give me no more methadone 
And they cut off your welfare check
STRING

puts "--6--"
name = "Jane"
age = 17
puts "#{name} is #{age} years old"

puts "--7--"
x = 5
y = 6
puts "The product of #{x} and #{y} is #{x*y}"

puts "--8--"
lang = "Ruby" + " programming" + " languge"
puts lang

lang = "Python" " programming" " language"
puts lang

lang = "Perl" << " programming" << " language"
puts lang

lang = "Java".concat(" programming").concat(" language")
puts lang

puts "--9--"
msg = "Jane"
msg << " is " 
msg << "17 years old"

puts msg

msg.freeze

puts "--10--"
puts "12" == "12"
puts "17" == "9"
puts "aa" == "ab"

puts "Jane".eql? "Jan"
puts "Jane".eql? "Jane"

puts "--11--"
#puts "a" <==> "b"
#puts "b" <==> "a"
#puts "a" <==> "a"

puts "--12--"
puts "Jane".casecmp "Jane"
puts "Jane".casecmp "jane"
puts "Jane".casecmp "Jan"

puts "--13--"
website = "google.com"
puts website

website = String.new "zetcode.com"
puts website

puts "--14--"
puts "zetcode".upcase
puts "zetcode".size
puts "zetcode".reverse

puts "--15--"
word = "Determination"

puts "The word #{word} has #{word.size} characters"

puts word.include? "tion"
puts word.include? "tic"

puts

puts word.empty?
#word.clear
puts word.empty?

puts "--16--"
ruby = "Ruby programming language"

puts ruby.upcase
puts ruby.downcase
puts ruby.capitalize
puts ruby.swapcase

puts "--17--"
ws1 = "zetcode.com"
ws2 = "www.gnome.org"
puts ws1.start_with? "www."
puts ws2.start_with? "www."
puts
puts ws1.end_with? ".com"
puts ws2.end_with? ".com"

puts "--18--"
msg = "Jane\t17\nThomas\t23"
puts msg
puts msg.inspect

puts "--19--"
print "proceed? (Yes/No) "

response = gets

if (response.downcase == "yes")
    puts "Downloaded"
else
    puts "Download cancelled"
end

puts response.inspect

puts "--20--"
print "Proceed? (Yes/No) "

response = gets

if (response.downcase.chomp == "yes")
    puts "yes"
else
    puts "No"
end

puts response.inspect

puts "--21--"
puts "There are %d oranges in the basket." % 12
puts "There are %d oranges and %d apples in the basket." % [12, 10]

puts "--22--"
puts "There are %d apples." % 5
puts "I can see %i oranges." % 3
puts "The width of iPhone 3G is %f mm." % 62.1
puts "This animal is called a %s" % "rhinoceros."

puts "--23--"
#stringexample = "zetcode.com"
#stringexample.each_char do |c|
#    print "#{c} has ASCII code %d\n" % c.ord    
#end

puts "--24--"
# decimal
puts "%d" % 300
# hexadecimal
puts "%x" % 300
# octal
puts "%o" % 300
# binary
puts "%b" % 300
# scientific
puts "%e" % (5/3.0)

puts "--25--"
puts 'Height: %f %s' % [172.3, 'cm']
puts 'Height: %.1f %s' % [172.3, 'cm']

puts "%d" % 16
puts "%.5d" % 16

puts "%s" % "zetcode"
puts "%.5s" % "zetcode"

puts "--26--"
puts "%d" % 1
puts "%d" % 16
puts "%d" % 165
puts "%d" % 1656
puts "%d" % 16567

puts "%10d" % 1
puts "%10d" % 16
puts "%10d" % 165
puts "%10d" % 1656
puts "%10d" % 16567

puts "--27--"
puts "%#b" % 231
puts "%#x" % 231
puts "%#o" % 231

puts "%.0e" % 231
puts "%#.0e" % 231

puts "%.0f" % 231
puts "%#.0f" % 231

puts "--28--"
puts "%d" % 231
puts "%+d" % 231
puts "%d" % -231
puts "%+d" % -231

puts "%b" % -231
puts "%o" % -231
puts "%x" % -231

puts "%+b" % -231
puts "%+o" % -231
puts "%+x" % -231

puts "--29--"
puts "%.*f" % [3, 1.1111111]
puts "%0*d" % [10, 2]
puts "%0*.*f" % [10, 3, 1.1111]

