from selenium import webdriver
from send_email import send_email
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
lnk = "https://summerofcode.withgoogle.com/archive/2020/organizations/"



# organization-card__container layout-row flex-xs-100 flex-sm-50 flex-33
# organization-card__container layout-row flex-xs-100 flex-sm-50 flex-33

try:
	driver.get(lnk)
finally:
	driver.quit()
# orgs = driver.find_element_by_xpath("/html/body/main/section/div/ul/li")

# organization-card__link md-soc-theme layout-row flex
# elems = driver.find_elements_by_css_selector("")
# elems = WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "organization-card__container layout-row flex-xs-100 flex-sm-50 flex-33")))
# elems = driver.find_element_by_class_name("fixed-width")
# print(elems.text)
# elems = driver.find_elemeny_by_xpath("/html/body/main/section/div/ul/li[1]")
# elems = driver.find_element_by_xpath("/html/body/main/section/div/ul")
# for i in elems:
	# print(i.text)
# elem = elems.find_element_by_tag_name("li")
# ele  = elem.find_element_by_tag_name("a")
# print(ele.text)
# /html/body/main/section/div/ul/li[6]
# h = elems.get_attribute('href')
# print(type(elems))
# for ele in elems:
	# el = elems.find_element_by_tag_name("li")
	# e = el.find_element_by_tag_name("a")
	# print(e.get_attribute('href'))
# el = ele.find_element_by_tag_name("a")
# print(type(ele))
# print(type(el))
# h = [i.get_attribute('href') for i in elems]
# print(h)
# elems = elems.find_element_by_tag_name("ul")
# print(elems.text)
# elems = driver.find_element_by_class_name("organization-card__container layout-row flex-xs-100 flex-sm-50 flex-33")
# print(elems)
# elems = elems.find_element_by_tag_name("li")
# elems = elems.find_element_by_tag_name("a")
driver.quit()

# print(links)
# lst = ['react', 'python', 'android', 'compiler', 'javascript', 'postgresql', 'java', 'coq', 'ocaml', 'rust', 'c/c++']
# print("List of Technologies:- ", lst)
# email = input("Enter email:- ")
# password = input("Enter password:- ")
# tech_lst = []
# ch = input("what you know from above tech stack:- ")
# while(ch != 'exit'):
# 	tech_lst.append(ch)
# 	ch = input("what you know from above tech stack:- ")

# print(tech_lst)