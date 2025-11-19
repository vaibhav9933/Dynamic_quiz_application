# run_quiz_fixed.py
import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
    TimeoutException,
    StaleElementReferenceException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

OUT_DIR = "artifacts"
SCREEN_DIR = os.path.join(OUT_DIR, "screenshots")
os.makedirs(SCREEN_DIR, exist_ok=True)

def take_screenshot(driver, name):
    path = os.path.join(SCREEN_DIR, name)
    driver.save_screenshot(path)
    print("Saved screenshot:", path)

def save_console_logs(driver, filepath):
    try:
        logs = driver.get_log("browser")
        with open(filepath, "w", encoding="utf-8") as f:
            for entry in logs:
                f.write(f"{entry['level']} {entry['message']}\n")
        print("Saved console logs:", filepath)
    except Exception as e:
        print("Could not fetch browser logs:", e)

def wait_for_options(driver, timeout=8):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".option")))

def wait_for_result(driver, timeout=6):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.visibility_of_element_located((By.ID, "resultBox")))

def main():
    # ---------- update only if index.html is elsewhere ----------
    local_index = os.path.abspath("index.html")
    url = "file:///" + local_index.replace("\\", "/")
    print("Opening:", url)
    # ------------------------------------------------------------

    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # don't use headless for recording
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.set_window_size(1280, 800)
    wait = WebDriverWait(driver, 8)

    try:
        driver.get(url)
        time.sleep(0.8)
        take_screenshot(driver, "landing.png")

        # Click Start
        try:
            start = wait.until(EC.element_to_be_clickable((By.ID, "startBtn")))
            start.click()
            time.sleep(0.8)
            take_screenshot(driver, "first_question.png")
        except TimeoutException:
            print("Start button not found/clickable.")
            return

        q_index = 1
        max_iterations = 200

        while q_index <= max_iterations:
            try:
                # Wait until at least one visible option is present
                options = wait_for_options(driver, timeout=10)
            except TimeoutException:
                # Maybe the quiz finished and result is shown
                try:
                    result = driver.find_element(By.ID, "resultBox")
                    if result.is_displayed():
                        take_screenshot(driver, "final_result.png")
                        break
                except NoSuchElementException:
                    print("No options found and no result box — stopping.")
                    break
                break

            # find the first truly visible & interactable option
            clicked = False
            for idx, opt in enumerate(options):
                try:
                    if not opt.is_displayed():
                        continue
                    # scroll into view
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", opt)
                    time.sleep(0.12)
                    try:
                        opt.click()
                    except (ElementNotInteractableException, StaleElementReferenceException):
                        # fallback to JS click
                        try:
                            driver.execute_script("arguments[0].click();", opt)
                        except Exception as e:
                            print(f"JS click failed on option {idx}: {e}")
                            continue
                    clicked = True
                    time.sleep(0.6)  # small wait for UI to update
                    take_screenshot(driver, f"after_select_q{q_index}.png")
                    q_index += 1
                    break
                except StaleElementReferenceException:
                    # item became stale, continue to next
                    continue

            if not clicked:
                # nothing clicked: maybe overlay or animation. wait then retry
                print("Could not click any visible option right now — waiting 0.6s and retrying.")
                time.sleep(0.6)
                # also check if result appeared in meantime
                try:
                    if driver.find_element(By.ID, "resultBox").is_displayed():
                        take_screenshot(driver, "final_result.png")
                        break
                except Exception:
                    pass
                continue

            # after clicking, wait briefly for either new options or result box
            try:
                # wait up to a few seconds for either new question or result
                WebDriverWait(driver, 5).until(
                    lambda d: len(d.find_elements(By.CSS_SELECTOR, ".option")) > 0 or
                              (d.find_elements(By.ID, "resultBox") and d.find_element(By.ID, "resultBox").is_displayed())
                )
            except TimeoutException:
                # not a problem; loop will attempt to find options again or detect result
                pass

            # if result appears, break
            try:
                if driver.find_element(By.ID, "resultBox").is_displayed():
                    take_screenshot(driver, "final_result.png")
                    break
            except Exception:
                pass

        # Save logs and print final score
        save_console_logs(driver, os.path.join(OUT_DIR, "console_logs.txt"))
        try:
            score_el = driver.find_element(By.ID, "score")
            print("Final score:", score_el.text)
        except NoSuchElementException:
            print("Score element not found.")

    finally:
        time.sleep(0.3)
        driver.quit()
        print("Done. Artifacts saved in:", OUT_DIR)

if __name__ == "__main__":
    main()
