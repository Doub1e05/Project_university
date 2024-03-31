[app]

version = 1.0
# (str) Название вашего приложения
title = CameraApp

# (str) Имя пакета вашего приложения
package.name = camera_app

# (str) Версия вашего приложения
package.version = 1.0

# (str) Путь к вашему основному файлу приложения (это может быть
# основной файл Python - '.py' или файл Kivy - '.kv')
source.dir = .

# (list) Используемые пакеты, модули, данные файлов
source.include_exts = py,png,jpg,kv,atlas

# (list) Пакеты, включенные в ваше приложение
# Разделенные запятой в формате org.test.MyName
package.domain = org.test
package.include.external_libs = python3, kivy

# (list) Какие папки (и файлы) следует исключить из сборки
# exclude_patterns = .git, __pycache__, .DS_Store, *.pyc, *.pyo, .idea, .kivy

# (list) Используемые модули, указанные в этом разделе, должны быть
# доступны в любом месте в вашем коде
# В этом примере это будет доступно в коде как import camera, import camera.filters
# import.camera = photobooth
# import.camera.filters = photofx, camshaders

# (list) Добавьте внешние python-модули здесь (опционально)
#android.permissions = CAMERA
#p4a.branch = develop

# (str) Пользовательские включаемые аргументы для платформы Android
# Android.permissions = CAMERA,INTERNET

# (int) Число изображений, которые будут кэшироваться при открытии
# Kivy 'image' объектов. По умолчанию: 128
# kivy_image = 128

# (int) Размер памяти, выделенный для SDL2 / ускорения (в мегабайтах)
# sdl2_mem = 128

# (str) Цель платформы для вашего приложения: см. Buildozer docs
target = android

# (list) Опции для сборщика средств разработки (включая -debug, -release, -vm, -32bit, -64bit, -p <имя профиля>)
# (если эти опции поддерживаются вашими средствами разработки)
# android.arch = armeabi-v7a
# android.gradle_dependencies = 'com.android.support:appcompat-v7:19.2.0'

# (bool) Указывает, следует ли использовать команду "--android --debug" при сборке
# debug = False

# (str) Иконка приложения
icon.filename = %(source.dir)s/icon.png

# (str) Путь к файлу вашего изображения иконки
icon.source = %(source.dir)s/icon.png

# (str) Версия приложения, используемая только для информации
# Возможно, что вы захотите изменить это для внутренней версии вашего приложения
# на каждом из различных выпусков.
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Пользовательские разрешения для Android
# android.permissions = INTERNET

# (list) Перечислите дополнительные инструменты / пакеты, требуемые вашим приложением:
# (по умолчанию, python3, kivy)
# android.whitelist = python3, kivy

# (str) Ключевое слово, используемое для подписи ваших приложений Android
# android.release.keystore = mykeystore.keystore
# android.release.keystore.password = mypassword
# android.release.keyalias = mykeyalias
# android.release.keyalias.password = mykeyaliaspassword

# (str) Список разделенных запятыми библиотек для статического анализа
# (через атрибуты AST)
# android.meta_data = com.google.android.gms.version=@integer/google_play_services_version