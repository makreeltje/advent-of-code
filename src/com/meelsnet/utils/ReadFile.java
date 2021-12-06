package com.meelsnet.utils;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;

public class ReadFile {
    public static Scanner readFile(String fileName) throws FileNotFoundException {
        return new Scanner(new BufferedReader(new FileReader("src/com/meelsnet/resources/" + fileName + ".txt")));
    }
}
