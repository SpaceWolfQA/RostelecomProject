import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import (valid_ls, valid_password, valid_phone, valid_email, valid_login, invalid_password, test_20_password,
                      test_21_password, test_7_password, test_8_password, valid_lastName, valid_firstName, invalid_email,
                      invalid_phone, invalid_firstName, invalid_lastName)



@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    chrome_options = Options()
    driver.implicitly_wait(10)  # in seconds
    # Переходим на страницу авторизации
    driver.get('https://lk.rt.ru/')

    yield driver

    driver.quit()


def test_auth_by_phone_without_pass(driver): #авторизация с помощью номера телефона по временному коду
    #в поле вводим валидный номер телефона
    driver.find_element(By.ID, 'address').send_keys(valid_phone)
    driver.find_element(By.ID, 'otp_get_code').click()
    assert driver.find_element(By.NAME, 'otp_back_phone').text == 'Изменить номер'

def test_auth_by_email_without_pass(driver): #авторизация с помощью email по временному коду
    #в поле вводим валидный email
    driver.find_element(By.ID, 'address').send_keys(valid_email)
    driver.find_element(By.ID, 'otp_get_code').click()
    assert driver.find_element(By.NAME, 'otp_back_phone').text == 'Изменить номер'

def test_auth_by_invalid_email_without_pass(driver): #авторизация с помощью невалидного email по временному коду
    # в поле вводим невалидный email
    driver.find_element(By.ID, 'address').send_keys(invalid_email)
    driver.find_element(By.ID, 'otp_get_code').click()
    assert WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
             '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div/span')))

def test_auth_by_phone_number_with_pass(driver): #авторизация по номеру телефона с паролем
    #Переходим на авторизацию с паролем
    driver.find_element(By.ID, 'standard_auth_btn').click()
    #переходим на авторизацию по телефону
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    # Вводим номер телефона
    driver.find_element(By.ID, 'username').send_keys(valid_phone)
    #Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    #Нажимаем авторизацию
    driver.find_element(By.ID, 'kc-login').click()
    assert WebDriverWait(driver, 20).until(EC.url_contains('start.rt.ru'))

def test_auth_by_email_with_pass(driver): #авторизация по почте с паролем
    #Переходим на авторизацию с паролем
    driver.find_element(By.ID, 'standard_auth_btn').click()
    #переходим на авторизацию по email
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    # Вводим email
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    #Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    #Нажимаем авторизацию
    driver.find_element(By.ID, 'kc-login').click()
    assert WebDriverWait(driver, 20).until(EC.url_contains('start.rt.ru'))

def test_auth_by_login_with_pass(driver): #авторизация по логину с паролем
    # Переходим на авторизацию с паролем
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # переходим на авторизацию по логину
    driver.find_element(By.ID, 't-btn-tab-login').click()
    # Вводим логин
    driver.find_element(By.ID, 'username').send_keys(valid_login)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Нажимаем авторизацию
    driver.find_element(By.ID, 'kc-login').click()
    assert WebDriverWait(driver, 20).until(EC.url_contains('start.rt.ru'))

def test_auth_by_ls_with_pass(driver): #авторизация по личевому счёту с паролем
    # Переходим на авторизацию с паролем
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # переходим на авторизацию по лицевому счёту
    driver.find_element(By.ID, 't-btn-tab-ls').click()
    # Вводим лицевой счёт
    driver.find_element(By.ID, 'username').send_keys(valid_ls)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Нажимаем авторизацию
    driver.find_element(By.ID, 'kc-login').click()
    assert WebDriverWait(driver, 20).until(EC.url_contains('start.rt.ru'))

def test_auth_by_invalid_email_with_pass(driver): #авторизация по невалидному email с паролем
    # Переходим на авторизацию с паролем
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # переходим на авторизацию по email
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    # Вводим невалидный email
    driver.find_element(By.ID, 'username').send_keys(invalid_email)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Нажимаем авторизацию
    driver.find_element(By.ID, 'kc-login').click()
    assert driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'

def test_auth_by_invalid_phone_with_pass(driver): #авторизация по невалидному телефону с паролем
    # Переходим на авторизацию с паролем
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # переходим на авторизацию по номеру телефона
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    # Вводим невалидный номер телефона
    driver.find_element(By.ID, 'username').send_keys(invalid_phone)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Нажимаем авторизацию
    driver.find_element(By.ID, 'kc-login').click()
    assert driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'

def test_auth_by_invalid_pass(driver): #авторизация по невалидному паролю
    # Переходим на авторизацию с паролем
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # переходим на авторизацию по номеру телефона
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    # Вводим невалидный номер телефона
    driver.find_element(By.ID, 'username').send_keys(valid_phone)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(invalid_password)
    # Нажимаем авторизацию
    driver.find_element(By.ID, 'kc-login').click()
    assert driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'

def test_valid_register(driver): #регистрация с валидными данными
    # Переходим на авторизацию с паролем
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # Выбираем регистрацию
    driver.find_element(By.ID, 'kc-register').click()
    # Заполняем все поля
    driver.find_element(By.NAME, 'firstName').send_keys(valid_firstName)
    driver.find_element(By.NAME, 'lastName').send_keys(valid_lastName)
    driver.find_element(By.ID, 'address').send_keys(valid_phone)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.ID, 'password-confirm').send_keys(valid_password)
    driver.find_element(By.NAME, 'register').click()
    assert driver.find_element(By.CLASS_NAME, 'card-container__title')

def test_invalid_pass_register(driver): #регистрация с невалидными данными (пароль)
    # Переходим на авторизацию с паролем
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # Выбираем регистрацию
    driver.find_element(By.ID, 'kc-register').click()
    # Заполняем все поля
    driver.find_element(By.NAME, 'firstName').send_keys(valid_firstName)
    driver.find_element(By.NAME, 'lastName').send_keys(valid_lastName)
    driver.find_element(By.ID, 'address').send_keys(valid_phone)
    driver.find_element(By.ID, 'password').send_keys(invalid_password)
    driver.find_element(By.ID, 'password-confirm').send_keys(invalid_password)
    driver.find_element(By.ID, 'password-confirm').click()
    assert WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
                                                    '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span')))


def test_different_pass_register(driver): #регистрация с другим паролем подтверждения
    # Переходим на авторизацию с паролем
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # Выбираем регистрацию
    driver.find_element(By.ID, 'kc-register').click()
    # Заполняем все поля
    driver.find_element(By.NAME, 'firstName').send_keys(valid_firstName)
    driver.find_element(By.NAME, 'lastName').send_keys(valid_lastName)
    driver.find_element(By.ID, 'address').send_keys(valid_phone)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.ID, 'password-confirm').send_keys(invalid_password)
    driver.find_element(By.NAME, 'register').click()
    assert WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
                                                                            '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[2]/span')))

def test_register_pass_7_symb(driver):  # регистрация с паролем в 7 символов
    # Переходим на авторизацию с паролем
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # Выбираем регистрацию
    driver.find_element(By.ID, 'kc-register').click()
    #Заполняем все поля
    driver.find_element(By.NAME, 'firstName').send_keys(valid_firstName)
    driver.find_element(By.NAME, 'lastName').send_keys(valid_lastName)
    driver.find_element(By.ID, 'address').send_keys(valid_phone)
    driver.find_element(By.ID, 'password').send_keys(test_7_password)
    driver.find_element(By.ID, 'password-confirm').send_keys(test_7_password)
    driver.find_element(By.NAME, 'register').click()
    assert (WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
            '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span'))).text ==
            'Длина пароля должна быть не менее 8 символов')

def test_register_pass_8_symb(driver):  # регистрация с паролем в 8 символов
    # Переходим на авторизацию с паролем
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # Выбираем регистрацию
    driver.find_element(By.ID, 'kc-register').click()
    # Заполняем все поля
    driver.find_element(By.NAME, 'firstName').send_keys(valid_firstName)
    driver.find_element(By.NAME, 'lastName').send_keys(valid_lastName)
    driver.find_element(By.ID, 'address').send_keys(valid_phone)
    driver.find_element(By.ID, 'password').send_keys(test_8_password)
    driver.find_element(By.ID, 'password-confirm').send_keys(test_8_password)
    driver.find_element(By.NAME, 'register').click()
    assert driver.find_element(By.CLASS_NAME, 'card-container__title')

def test_register_pass_20_symb(driver):  # регистрация с паролем в 20 символов
    # Переходим на авторизацию с паролем
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # Выбираем регистрацию
    driver.find_element(By.ID, 'kc-register').click()
    # Заполняем все поля
    driver.find_element(By.NAME, 'firstName').send_keys(valid_firstName)
    driver.find_element(By.NAME, 'lastName').send_keys(valid_lastName)
    driver.find_element(By.ID, 'address').send_keys(valid_phone)
    driver.find_element(By.ID, 'password').send_keys(test_20_password)
    driver.find_element(By.ID, 'password-confirm').send_keys(test_20_password)
    driver.find_element(By.NAME, 'register').click()
    assert driver.find_element(By.CLASS_NAME, 'card-container__title')

def test_register_pass_21_symb(driver):  # регистрация с паролем в 21 символ
    # Переходим на авторизацию с паролем
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # Выбираем регистрацию
    driver.find_element(By.ID, 'kc-register').click()
    # Заполняем все поля
    driver.find_element(By.NAME, 'firstName').send_keys(valid_firstName)
    driver.find_element(By.NAME, 'lastName').send_keys(valid_lastName)
    driver.find_element(By.ID, 'address').send_keys(valid_phone)
    driver.find_element(By.ID, 'password').send_keys(test_21_password)
    driver.find_element(By.ID, 'password-confirm').send_keys(test_21_password)
    driver.find_element(By.NAME, 'register').click()
    assert (WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
            '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span'))).text ==
            'Длина пароля должна быть не более 20 символов')

def test_register_invalid_phone(driver):  # регистрация с невалидным номером телефона
    # Переходим на авторизацию с паролем
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # Выбираем регистрацию
    driver.find_element(By.ID, 'kc-register').click()
    # Заполняем все поля
    driver.find_element(By.NAME, 'firstName').send_keys(valid_firstName)
    driver.find_element(By.NAME, 'lastName').send_keys(valid_lastName)
    driver.find_element(By.ID, 'address').send_keys(invalid_phone)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.ID, 'password-confirm').send_keys(valid_password)
    driver.find_element(By.NAME, 'register').click()
    assert WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
                                                                            '//*[@id="page-right"]/div/div[1]/div/form/div[3]/div/span')))

def test_register_invalid_firstName(driver):  # регистрация с невалидным именем
    # Переходим на авторизацию с паролем
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # Выбираем регистрацию
    driver.find_element(By.ID, 'kc-register').click()
    # Заполняем все поля
    driver.find_element(By.NAME, 'firstName').send_keys(invalid_firstName)
    driver.find_element(By.NAME, 'lastName').send_keys(valid_lastName)
    driver.find_element(By.ID, 'address').send_keys(invalid_phone)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.ID, 'password-confirm').send_keys(valid_password)
    driver.find_element(By.NAME, 'register').click()
    assert (WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
            '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/span'))).text ==
            'Необходимо заполнить поле кириллицей. От 2 до 30 символов.')

def test_register_invalid_lastName(driver):  # регистрация с невалидной фамилией
    # Переходим на авторизацию с паролем
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # Выбираем регистрацию
    driver.find_element(By.ID, 'kc-register').click()
    # Заполняем все поля
    driver.find_element(By.NAME, 'firstName').send_keys(invalid_firstName)
    driver.find_element(By.NAME, 'lastName').send_keys(invalid_lastName)
    driver.find_element(By.ID, 'address').send_keys(invalid_phone)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.ID, 'password-confirm').send_keys(valid_password)
    driver.find_element(By.NAME, 'register').click()
    assert (WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
            '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/span'))).text ==
            'Необходимо заполнить поле кириллицей. От 2 до 30 символов.')

def test_invalid_register(driver):  # регистрация со всеми невалидными полями
    # Переходим на авторизацию с паролем
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # Выбираем регистрацию
    driver.find_element(By.ID, 'kc-register').click()
    # Заполняем все поля
    driver.find_element(By.NAME, 'firstName').send_keys(invalid_firstName)
    driver.find_element(By.NAME, 'lastName').send_keys(invalid_lastName)
    driver.find_element(By.ID, 'address').send_keys(invalid_phone)
    driver.find_element(By.ID, 'password').send_keys(invalid_password)
    driver.find_element(By.ID, 'password-confirm').send_keys(invalid_password)
    driver.find_element(By.NAME, 'register').click()
    assert (WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
                                                                             '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/span'))).text ==
            'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'), (WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
            '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/span'))).text ==
            'Необходимо заполнить поле кириллицей. От 2 до 30 символов.')
    assert WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
                                                                            '//*[@id="page-right"]/div/div[1]/div/form/div[3]/div/span')))
    assert WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
                                                                            '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[2]/span')))
    assert WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,
                                                    '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span')))

def test_re_registr(driver): #регистрация с уже имеющимися данными
    # Переходим на авторизацию с паролем
    driver.find_element(By.ID, 'standard_auth_btn').click()
    # Выбираем регистрацию
    driver.find_element(By.ID, 'kc-register').click()
    # Заполняем все поля
    driver.find_element(By.NAME, 'firstName').send_keys(valid_firstName)
    driver.find_element(By.NAME, 'lastName').send_keys(valid_lastName)
    #Примечание: вводимый номер телефона или email УЖЕ ДОЛЖЕН БЫТЬ зарегистрирован в системе
    driver.find_element(By.ID, 'address').send_keys(valid_phone)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.ID, 'password-confirm').send_keys(valid_password)
    driver.find_element(By.NAME, 'register').click()
    assert driver.find_element(By.CLASS_NAME, 'card-modal__title').text == 'Учётная запись уже существует'