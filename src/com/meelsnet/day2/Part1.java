package com.meelsnet.day2;

import com.meelsnet.utils.ReadFile;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Part1 {
    public static void main(String[] args) throws FileNotFoundException {
        File input = ReadFile.readFile("input-day2.txt");
        Scanner reader = new Scanner(input);

        var depth = 0;
        var horizontal = 0;

        while (reader.hasNextLine()) {
            var data = reader.nextLine();
            var command = data.split(" ")[0];
            var amount = Integer.parseInt(data.split(" ")[1]);

            switch (command) {
                case "forward":
                    horizontal += amount;
                    break;
                case "down":
                    depth += amount;
                    break;
                case "up":
                    depth -= amount;
                    break;
            }
        }
        System.out.println(horizontal * depth);

    }
}
