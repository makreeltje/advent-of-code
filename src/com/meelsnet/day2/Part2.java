package com.meelsnet.day2;

import com.meelsnet.utils.ReadFile;

import java.io.FileNotFoundException;
import java.util.Scanner;

public class Part2 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner reader = ReadFile.readFile("input-day2");

        var depth = 0;
        var horizontal = 0;
        var aim = 0;

        while (reader.hasNextLine()) {
            var data = reader.nextLine();
            var command = data.split(" ")[0];
            var amount = Integer.parseInt(data.split(" ")[1]);

            switch (command) {
                case "forward":
                    horizontal += amount;
                    depth += aim * amount;
                    break;
                case "down":
                    aim += amount;
                    break;
                case "up":
                    aim -= amount;
                    break;
            }
        }
        System.out.println(horizontal * depth);
    }
}
