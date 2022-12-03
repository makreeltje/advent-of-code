package com.meelsnet.day3;

import com.meelsnet.utils.ReadFile;

import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Part2 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner reader = ReadFile.readFile("input-day3");

        List<String> data = new ArrayList<>();
        List<String> filteredData = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        StringBuilder sbGamma = new StringBuilder();
        StringBuilder sbEpsilon = new StringBuilder();
        while (reader.hasNextLine()) {
            data.add(reader.nextLine());
        }

        int zero = 0;
        int one = 0;
        for (int i = 0; i < 12; i++) {
            for (String value : data) {
                sb.append(value.charAt(i));
            }
            for (int j = 0; j < sb.length()-1; j++) {
                if(sb.charAt(j) == '0'){
                    zero++;
                } else {
                    one++;
                }
            }
            if(one > zero){
                for (String value : data) {
                    
                }
            } else {
                for (String value : data) {
                    sb.append(value.charAt(i));
                }
            }
            one = 0;
            zero = 0;
            sb.setLength(0);
        }

        System.out.println(Integer.parseInt(sbGamma.toString(),2)*Integer.parseInt(sbEpsilon.toString(),2));
    }

    private static void filterData(List<String> data){

    }
}
