from pages.base_page import BasePage


class Dasboard(BasePage):
    button_xpath = "//*[@id='login']"
    main_page_button = "//button[text()='Main page']"
    players_button = "//button[text()='Players']"
    language_button = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    wyloguj_buton = "//*[@id='__nex']/div[1]/div/div/div/ul[2]/div[2]"
    add_player_button = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    dev_team_contact = "//button[text()='DEV TEAM CONTACT']"
    last_created = "//button[text()='Last created player']"
    last_updated_player = "//button[text()='Last updated player']"
    players_count = "//*[@id='__next']/div[1]/main/div[2]/div[1]/div"


