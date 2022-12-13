SIZE = 20                                   # Размер шрифта
W_H = 1.7                                   # Отношение высоты к ширене
DELTA_POSITION = 5                          # Максимальный отступ сверху

MEAN_W_SIZE_WORD = round(5.5 * SIZE/W_H)    # Средняя ширина картинки слова (в русском письменом языке 5.5)
H_SIZE = SIZE+DELTA_POSITION                # Средняя высота картинки слова
M = MEAN_W_SIZE_WORD*H_SIZE                 # Число пикселей в картинки
START_X = 0                                 # Начальная точка положения, отколибровать можно по 2 буквам fp
START_Y = -3                                

# #ШРИФТЫ
# TNR_reg = 'font/TimesNewRomanCyr_Regular.ttf'
# TNR_bold = 'font/TimesNewRomanCyr_Bold.ttf'

# Шрифт хранится как font/{name_font}_{type_font}.ttf'
TYPE_FONTS = ["Regular", "Bold", "Italic"]
NAME_FONTS = ["TimesNewRomanCyr", "ArialCyr", "Calibri", "Verdana"] 

# TYPE_FONT = [TNR_reg, TNR_bold]

# Имя модели
NAME_MODEL = "model_3"

# Кол-во слов (max 10000)
COUNT_WORDS = 300

# Настройки Tesseract
CONFIG_TESSERACT = '-l rus+eng --oem 3 --psm 11'

# Настройки окна 
NAME_WINDOW_IMG = "img"
SIZE_H_WINDOW = 600
SIZE_W_WINDOW = 400

# Настройки стиля
BOLD_COLOR = (0, 255, 0)
REGULAR_COLOR = (0, 255, 255)
ITALIC_COLOR = (255, 0, 0)
MY_CROP = True
# Настройка проверок
CONF = 0
MIN_H = 5
MIN_W = 10

