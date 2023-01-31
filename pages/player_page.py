from pages.base_page import BasePage


class PlayerPage(BasePage):
    email = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[1]/div"
    phone = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[4]"
    name = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[4]"
    surname = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[3]"
    weight = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[5]/div"
    
    pass
