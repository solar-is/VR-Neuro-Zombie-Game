package com.mprosolovich;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException, InterruptedException {
        while (true) {
            System.out.println("Do you want to read data from stdin(1) or from file(2) ?");
            Scanner scanner = new Scanner(System.in);
            String input = scanner.nextLine();
            if (input.trim().equals("2")) {
                Thread.sleep(1000);
                for (String lineFromFile : Files.readAllLines(Path.of(System.getProperty("user.dir") + "\\pulse.txt"))) {
                    send(lineFromFile);
                }
            } else {
                send(scanner.nextLine());
            }
        }
    }

    static void send(String value) throws InterruptedException, IOException {
        long start = System.currentTimeMillis();
        Thread.sleep(1000);
        URL url = new URL("http://127.0.0.1:8000/hr/update/?bpm=" + value);
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("GET");
        int responseCode = con.getResponseCode();
        assert responseCode == 200;
        con.disconnect();
        System.out.println("Successfully updated with value " + value + " in " + (System.currentTimeMillis() - start) + " ms");
    }
}
