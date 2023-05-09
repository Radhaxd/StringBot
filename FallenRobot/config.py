class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 28564672
    API_HASH = "89cf205dd07d743a6a869817e559d503"

    CASH_API_KEY = "5YJWIIKG5AUQ73A7"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://tmugvibv:Wo86qFDdNUczEGZuKI7zEeAxTKJLzI17@tiny.db.elephantsql.com/tmugvibv"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001605285063)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Shivam0:shivam098@cluster0.m80uulq.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/581cbe3c457ff23e8baaa.jpg"

    SUPPORT_CHAT = "Earn_without_investment01"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5953802361:AAHQHiOv_hzZ0BrkKlda90csrSz7t5PW_kc"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "MRW0DO9TOKQB"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1983049881  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
