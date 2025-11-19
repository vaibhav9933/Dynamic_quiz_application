package com.example.quiz;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.logging.LogEntry;
import org.openqa.selenium.logging.LogType;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.*;
import java.nio.file.*;
import java.time.Duration;
import java.util.List;

public class TestQuiz {
    public static void main(String[] args) throws Exception {
        // 1) Prepare output folders
        Path out = Paths.get("artifacts");
        Files.createDirectories(out);
        Path screenshots = out.resolve("screenshots");
        Files.createDirectories(screenshots);

        // 2) Setup driver
        WebDriverManager.chromedriver().setup();
        ChromeDriver driver = new ChromeDriver();
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

        try {
            // 3) Open local quiz (update path if needed)
            String pathToIndex = Paths.get("..","..","..","..","index.html").toAbsolutePath().toString();
            // if index.html is in a different place, replace above with absolute path like "file:///C:/quiz/index.html"
            String url = "file:///" + pathToIndex.replace("\\","/");
            driver.get(url);
            System.out.println("Opened: " + url);
            Thread.sleep(1000);

            // Screenshot - landing
            takeScreenshot(driver, screenshots.resolve("landing.png").toString());

            // Start quiz
            WebElement startBtn = driver.findElement(By.id("startBtn"));
            startBtn.click();
            wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("question")));
            takeScreenshot(driver, screenshots.resolve("question1.png").toString());

            // Loop through questions by detecting options
            for (int q = 1; q <= 20; q++) { // 20 is safe upper; break when no question
                List<WebElement> options = driver.findElements(By.cssSelector(".option"));
                if (options.isEmpty()) break;

                // select first available option (or pick logic by index)
                options.get(0).click();
                Thread.sleep(800);

                // screenshot for this step
                takeScreenshot(driver, screenshots.resolve("after_select_q" + q + ".png").toString());

                // wait a bit for next question to load or result page
                Thread.sleep(1000);

                // if result page visible, break
                if (driver.findElements(By.id("resultBox")).size() > 0 && driver.findElement(By.id("resultBox")).isDisplayed()) {
                    takeScreenshot(driver, screenshots.resolve("final_result.png").toString());
                    break;
                }
            }

            // Save browser console logs
            saveConsoleLogs(driver, out.resolve("console_logs.txt"));

            // Print final score if present
            List<WebElement> scoreEl = driver.findElements(By.id("score"));
            if (!scoreEl.isEmpty()) System.out.println("Score: " + scoreEl.get(0).getText());

        } finally {
            // small delay so video capture can catch the final screen
            Thread.sleep(800);
            driver.quit();
            System.out.println("Driver closed. Artifacts saved to ./artifacts/");
        }
    }

    private static void takeScreenshot(WebDriver driver, String filePath) throws IOException {
        File src = ((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE);
        Files.copy(src.toPath(), Paths.get(filePath), StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Saved screenshot: " + filePath);
    }

    private static void saveConsoleLogs(WebDriver driver, Path outFile) throws IOException {
        StringBuilder sb = new StringBuilder();
        List<LogEntry> entries = driver.manage().logs().get(LogType.BROWSER).getAll();
        for (LogEntry e : entries) {
            sb.append(e.getLevel()).append(" ").append(e.getMessage()).append(System.lineSeparator());
        }
        Files.write(outFile, sb.toString().getBytes());
        System.out.println("Saved console logs to " + outFile.toString());
    }
}
