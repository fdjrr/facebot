from selenium import webdriver
from faker import Faker
import string
import random

#    ____             ___       __
#   / __/__ ________ / _ )___  / /_
#  / _// _ `/ __/ -_) _  / _ \/ __/
# /_/  \_,_/\__/\__/____/\___/\__/
# Create Account Facebook using Selenium.


class FaceBot():
    def __init__(self, url) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.characters = list(string.ascii_letters +
                               string.digits + "!@#$%^&*()")
        self.fake = Faker()
        self.fullName = self.fake.name().split(" ")
        self.emailAddr = self.fake.email().split(
            "@")[0] + "@kjkszpjcompany.com"
        self.password = self.passwordGenerator(10)
        pass

    def passwordGenerator(self, length):
        random.shuffle(self.characters)
        password = []
        for x in range(int(length)):
            password.append(random.choice(self.characters))
        random.shuffle(password)
        return "".join(password)

    def create(self):
        print("[*] Full Name : {}".format(self.fullName))
        print("[*] Email Address : {}".format(self.emailAddr))
        print("[*] Password : {}".format(self.password))

        firstNameInput = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/form/div[3]/div[3]/div/div/div[1]/div[1]/div[2]/div/input")
        firstNameInput.send_keys(self.fullName[0])

        surNameInput = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/form/div[3]/div[3]/div/div/div[1]/div[2]/div[2]/div/input")
        surNameInput.send_keys(self.fullName[1])

        nextButton = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/form/div[9]/div[2]/button[1]")
        nextButton.click()

        dayOfBirth = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/form/div[4]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/select/option[4]")
        dayOfBirth.click()

        monthOfBirth = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/form/div[4]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/select/option[5]")
        monthOfBirth.click()

        yearOfBirth = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/form/div[4]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/select/option[24]")
        yearOfBirth.click()

        nextButton = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/form/div[9]/div[2]/button[1]")
        nextButton.click()

        signUpWithEmailAddress = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/form/div[11]/div/a[1]")
        signUpWithEmailAddress.click()

        inputEmailAddress = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/form/div[5]/div[3]/div/div/div[1]/div[3]/div[1]/input")
        inputEmailAddress.send_keys(self.emailAddr)

        nextButton = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/form/div[9]/div[2]/button[1]")
        nextButton.click()

        checkBoxGender = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/form/div[6]/div[3]/div/div/div[3]/div/label[2]/div/div/div[2]/input")
        checkBoxGender.click()

        nextButton = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/form/div[9]/div[2]/button[1]")
        nextButton.click()

        inputPassword = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/form/div[7]/div[3]/div/div/div[1]/div[2]/div/input")
        inputPassword.send_keys(self.password)

        signUpButton = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/form/div[9]/div[2]/button[4]")
        signUpButton.click()
        pass


if __name__ == "__main__":
    FaceBot = FaceBot(
        "https://m.facebook.com/reg/?cid=103&refsrc=deprecated&hrc=1&soft=hjk")
    FaceBot.create()
    pass
