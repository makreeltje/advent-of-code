package com.meelsnet.day1;

import com.meelsnet.utils.ReadFile;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Part1 {
    public static void main(String[] args) throws FileNotFoundException {
        File input = ReadFile.readFile("input-day1.txt");
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
        System.out.println(numberOfTimesIncreased);
    }
}
