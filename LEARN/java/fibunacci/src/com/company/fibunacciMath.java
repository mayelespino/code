package com.company;

/**
 * Created by mayelespino on 6/24/17.
 */

public class fibunacciMath {
    public Double calculate(int number) {
        Double root5 = Math.sqrt(5.0);
        Double gr = (1 + root5) / 2.0;
        Double igr = 1 - gr;
        Double value = (Math.pow(gr, number) - Math.pow(igr, number)) / root5;
        //return(Math.round(value));
        return(value);
    }
}
