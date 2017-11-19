--
-- Created by IntelliJ IDEA.
-- User: mayelespino
-- Date: 11/14/17
-- Time: 11:11 PM
-- To change this template use File | Settings | File Templates.
--

-- defines a factorial function
function fact (n)
    if n == 0 then
        return 1
    else
        return n * fact(n-1)
    end
end

-- print("enter a number:")
-- a = io.read("*number")        -- read a number
print(fact(10))
