package com.meelsnet.utils;

import java.io.File;

public class ReadFile {
    public static File readFile(String fileName){
        return new File("src/com/meelsnet/resources/" + fileName);
    }
}
