package com.company;

import java.io.FileOutputStream;

public class Main2 {

    public static void main(String[] args) {
        readFile("output.txt");
    }

    private static void readFile(String fileName) {
        try{
            FileOutputStream fout = new FileOutputStream(fileName);
            String s = "teścik.";
            byte b[] = s.getBytes();
            fout.write(b);
            fout.close();
        }catch(Exception e){ e.printStackTrace(); }
    }
}
