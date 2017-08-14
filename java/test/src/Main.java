import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.lang.String;

public class Main {

    public static void main(java.lang.String[] args) {
        java.lang.String[] values = java.lang.String[3];
        values[0]="{";
        values[1]= "{";
        values[2]="]";
        int sumParen = 0;
        int sumSquare = 0;
        int sumCurly = 0;
        for(int index = 0; index < values.length; ++index)
        {
            if(values[index] == "(") {++sumParen;}
            if(values[index] == "[") {++sumSquare;}
            if(values[index] == "{" ) {++sumCurly;}
            if(values[index] == ")") {
                --sumParen;
                if(sumParen != sumSquare || sumParen != sumCurly) break;
            }
            if(values[index] == "]") {
                --sumSquare;
                if(sumSquare != sumParen || sumSquare != sumCurly) break;
            }
            if(values[index] == "}" ) {
                ++sumCurly;
                if(sumCurly != sumParen || sumCurly != sumSquare) break;
            }
            System.out.println("x");
            System.out.println(sumParen);
            System.out.println(sumCurly);
            System.out.println(sumSquare);


        }
        java.lang.String[] returnArray = new java.lang.String[1];
        if((sumParen + sumCurly + sumSquare) > 0 ){
            returnArray[0]="NO";
        }
        else
        {
            returnArray[0]="YES";
        }
        System.out.println(returnArray);


    }
}
