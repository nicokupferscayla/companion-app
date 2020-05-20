from application import application


def logger(text: str):
    print(text)
    application.setInfo(text)
