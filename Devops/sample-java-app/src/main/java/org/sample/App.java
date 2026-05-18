package org.sample;

import java.io.InputStream;
import java.util.Scanner;

public class App {
    public static void main(String[] args) {

        InputStream inputStream =
                App.class.getClassLoader().getResourceAsStream("message.txt");

        Scanner scanner = new Scanner(inputStream);

        while (scanner.hasNextLine()) {
            System.out.println(scanner.nextLine());
        }
    }
}
