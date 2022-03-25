package com.company;

public class Main4 {
    static int[] CRC_TABLE = new int[256];

    public static void main(String[] args) {
        for (int i = 0; i < 256; ++i) {
            int code = i;
            for (int j = 0; j < 8; ++j) {
                code = ((code & 0x01) > 0 ? 0xEDB88320 ^ (code >>> 1) : (code >>> 1));
            }
            CRC_TABLE[i] = code;
        }
        System.out.println(crc32("This is example text..."));
    }

    private static int crc32(String text) {
        int crc = -1;
        for (int i = 0; i < text.length(); ++i) {
            int code = text.codePointAt(i);
            crc = CRC_TABLE[(code ^ crc) & 0xFF] ^ (crc >>> 8);
        }
        return (-1 ^ crc) >>> 0;
    }
}
