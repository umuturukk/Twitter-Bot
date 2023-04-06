from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en, en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options = self.browserProfile)
        self.username = username
        self.password = password

    # Giriş Yapma Metodu
    def signIn(self):
        self.browser.get('https://twitter.com/login') # Twitter Login sayfasını get() metodu ile çekiyoruz.
        self.browser.maximize_window() # Tarayıcımızı maximize_window() metodu ile tam ekran yapıyoruz.
        sleep(2) # Inputları girebilmek için birkaç saniye bekletiyoruz.
        usernameInput = self.browser.find_element(By.TAG_NAME, "input") # Username input'u tag_name input olacak şekilde find_element() metoduyla seçiyoruz.
        usernameInput.send_keys(self.username) # Seçmiş olduğumuz inputa kullanıcı adımızı gönderiyoruz.
        sleep(2)
        self.browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]").click() # İlerle butonuna tıklıyoruz.
        sleep(2)
        passwordInput = self.browser.find_element(By.XPATH, "//input[@type='password']") # Password input seçme işlemi.
        passwordInput.send_keys(self.password) # Şifreyi inputa yazdırma işlemi.
        self.browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div").click() # Giriş yap butonuna basma işlemi.
        sleep(5) # İşte! Artık başarılı bir şekilde giriş işlemini gerçekleştirdik.         

    # Keyword Girerek Arama
    def keywordSearch(self, keyword):
        url = "https://twitter.com/search?q=" + keyword + "&src=typed_query&f=top"
        self.browser.get(url)
    
    def getTrendTweetsTitle(self):
        trendTweetsTitle1 = self.browser.find_elements(By.XPATH, "//div[@data-testid='trend']/div/div[2]/span/span") # Trend olan tweetlerin başlıkları.
        trendTweetsTitle2 = self.browser.find_elements(By.XPATH, "//div[@data-testid='trend']/div/div[2]/span") # Trend olan tweetlerin başlıkları.
        trendTweetsTitleList = list()
        for i in trendTweetsTitle1:
            a = i.text
            trendTweetsTitleList.append(a)
        for i in trendTweetsTitle2:
            a = i.text
            trendTweetsTitleList.append(a)
        tr = set(trendTweetsTitleList)
        trendTweetsTitleList = list(tr)
        for i, j in enumerate(trendTweetsTitleList):
            print(f"{i+1}.tweet'in konu başlığı  '{j}'.")
        sleep(2)
