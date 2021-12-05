package com.meelsnet;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws FileNotFoundException {
        File input = new File("src/com/meelsnet/input.txt");
        part1(input);
        part2(input);

    }

    public static void part1(File input) throws FileNotFoundException {
        Scanner reader = new Scanner(input);

        var oldValue = 191;
        var numberOfTimesIncreased = 0;

        while (reader.hasNextLine()) {
            var data = Integer.parseInt(reader.nextLine());
            if (data > oldValue){
                numberOfTimesIncreased++;
            }
            oldValue = data;
        }
        System.out.println("part1: " + numberOfTimesIncreased);
    }

    public static void part2(File input) throws FileNotFoundException {
        Scanner reader = new Scanner(input);

        var oldValue = 564;
        var numberOfTimesIncreased = 0;

        var value1 = reader.nextLine();
        var value2 = reader.nextLine();
        var value3 = reader.nextLine();

        var sum = Integer.parseInt(value1) + Integer.parseInt(value2) +Integer.parseInt(value3);
        int i = 0;

        while (reader.hasNextLine()) {
            if(i==0) {
                value1 = reader.nextLine();
                i++;
            } else if(i==1) {
                value2 = reader.nextLine();
                i++;
            } else if(i==2) {
                value3 = reader.nextLine();
                i=0;
            }

            sum = Integer.parseInt(value1) + Integer.parseInt(value2) +Integer.parseInt(value3);

            if (sum > oldValue) {
                numberOfTimesIncreased++;
            }
            oldValue = sum;
        }
        System.out.println("part2: " + numberOfTimesIncreased);
    }
}
