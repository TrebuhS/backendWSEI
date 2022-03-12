package com.company;

import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.Date;

public class Main5 {
    public static void main(String[] args) {
        System.out.println(getLocalDate());
        System.out.println(getGlobalDate());
    }

    public static String getLocalDate() {
        Date date = new Date();
        return date.getHours() + ":" + date.getMinutes();
    }

    public static String getGlobalDate() {
        ZonedDateTime date = ZonedDateTime.now(ZoneId.of("Europe/Paris"));
        return date.getHour() + ":" + date.getMinute();
    }
}
