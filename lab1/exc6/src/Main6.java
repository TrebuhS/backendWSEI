package com.company;

import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

public class Main6 {
    public static void main(String[] args) {
        String text = "Rozbijam\nSobie\nStringa\nNa\nLinijki";
        String[] splitText = splitString(text);
        List<String> numberedLinesList =
                IntStream.range(0, splitText.length)
                        .mapToObj(index -> splitText[index] + " - " + index)
                        .toList();
        System.out.println(numberedLinesList);
    }

    private static String[] splitString(String string) {
        return string.split("\n");
    }
}
