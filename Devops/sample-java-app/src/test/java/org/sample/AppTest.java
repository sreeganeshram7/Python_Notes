package org.sample;

import java.io.InputStream;
import java.util.Scanner;

public class AppTest {
    public static void main(String[] args) {

        InputStream inputStream =
                AppTest.class.getClassLoader().getResourceAsStream("data.txt");

        Scanner scanner = new Scanner(inputStream);

        while (scanner.hasNextLine()) {
            System.out.println(scanner.nextLine());
        }
    }
}
