#!/usr/bin/ruby

def return_block
    yield
end

def return_proc( &proc ) yield
end

return_block { puts "Got block!" }
return_proc { puts "Got block, convert to proc!" }