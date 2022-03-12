package com.company;

import java.io.FileInputStream;
import java.io.IOException;

public class Main1 {

    public static void main(String[] args) {
        readFile("test.txt");
    }

    private static void readFile(String fileName) {
        try (FileInputStream fis = new FileInputStream(fileName)) {
            int content;
            while ((content = fis.read()) != -1) {
                System.out.print((char)content);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
