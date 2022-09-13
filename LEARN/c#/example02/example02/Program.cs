using System;

// top-level instructions examples

Console.WriteLine("Hello example02 !");
int x = 3;
LocalMethod();

void LocalMethod() { Console.WriteLine(x); } // Can access local variable

// Can access args
foreach (string arg in Environment.GetCommandLineArgs())
{
    Console.WriteLine(arg);
}

return (0); // can return a value to the caller (OS?)
