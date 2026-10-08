usrname= {
    "Ендрю" : {"password": "капібара","grades": [10,4,8,3,12,5]},
    "Пес патрон": {"password": "анчоус","grades": [11,12,9,2,7]},
    "Пасат": {"password": "зелений","grades": [4,3,5,4,6,10]},
    "Тузік": {"password": "собака","grades": [10,4,12,8,12,7]},
    "Матвій": {"password": "агурчік","grades": [5,2,6,7,12,11,8]}
}
login= input("Введіть логін:")
password=input("Введіть пароль:")
if login in usrname and usrname[login] ["password"]== password:
    user=usrname[login]
    grades= user["grades"]
    print("Вхід успішний!")
    print(f"Ваші оцінки: {grades} ")
    zadovoleno=0
    nezadovoleno=0
    for grade in grades:
        if 5<= grade <=12:
            zadovoleno += 1
        elif 1 <= grade <= 4:
            nezadovoleno +=1
    print(f"Кількість задовільних оцінок (5-12): {zadovoleno}")
    print(f"Кількість незадовільних оцінок (1-4): {nezadovoleno}")
else:
    print("Помилка: невірний пароль або логін!")