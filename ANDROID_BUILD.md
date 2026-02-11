# Инструкция по сборке для Android / Android Build Instructions

## Подробное руководство по сборке APK с использованием Buildozer

### Подготовка окружения / Environment Setup

#### 1. Требования к системе / System Requirements

**Операционная система / Operating System:**
- Ubuntu 20.04 LTS или новее (рекомендуется)
- Ubuntu 22.04 LTS (recommended)
- Debian 11+
- Другие Linux дистрибутивы (с адаптацией команд)

**Аппаратные требования / Hardware Requirements:**
- Минимум 8 GB RAM (рекомендуется 16 GB)
- Минимум 20 GB свободного места на диске
- Процессор с поддержкой виртуализации (для эмулятора)

#### 2. Установка системных зависимостей / Installing System Dependencies

```bash
# Обновление системы / Update system
sudo apt update
sudo apt upgrade -y

# Установка базовых инструментов / Install basic tools
sudo apt install -y git zip unzip curl wget

# Установка Java Development Kit 17 / Install JDK 17
sudo apt install -y openjdk-17-jdk

# Проверка установки Java / Verify Java installation
java -version
javac -version

# Установка Python и pip / Install Python and pip
sudo apt install -y python3 python3-pip python3-dev

# Установка библиотек для сборки / Install build libraries
sudo apt install -y build-essential libssl-dev libffi-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev

# Установка зависимостей Kivy / Install Kivy dependencies
sudo apt install -y libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev

# Установка дополнительных инструментов / Install additional tools
sudo apt install -y autoconf libtool pkg-config cmake ninja-build ccache
```

#### 3. Настройка переменных окружения / Setting Environment Variables

Добавьте в `~/.bashrc` или `~/.zshrc`:

```bash
# Java
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH

# Android SDK (будет создано Buildozer)
export ANDROID_SDK_ROOT=$HOME/.buildozer/android/platform/android-sdk
export PATH=$ANDROID_SDK_ROOT/tools:$ANDROID_SDK_ROOT/platform-tools:$PATH
```

Применить изменения / Apply changes:
```bash
source ~/.bashrc
```

#### 4. Установка Buildozer и Cython / Installing Buildozer and Cython

```bash
# Установка последних версий / Install latest versions
pip3 install --upgrade pip
pip3 install --upgrade buildozer
pip3 install --upgrade cython

# Проверка установки / Verify installation
buildozer --version
```

### Сборка приложения / Building the Application

#### Шаг 1: Клонирование репозитория / Step 1: Clone Repository

```bash
git clone https://github.com/Slava47/calclog.git
cd calclog
```

#### Шаг 2: Проверка файлов / Step 2: Verify Files

Убедитесь, что присутствуют все необходимые файлы:

```bash
ls -la
# Должны быть: main.py, buildozer.spec, requirements.txt
```

#### Шаг 3: Настройка buildozer.spec / Step 3: Configure buildozer.spec

Отредактируйте `buildozer.spec` при необходимости:

```ini
# Название приложения
title = Калькулятор Уравнений

# Имя пакета (только латинские буквы, цифры, подчеркивания)
package.name = calclog

# Домен пакета
package.domain = org.calclog

# Версия приложения
version = 1.0

# Ориентация экрана (portrait, landscape, sensor, all)
orientation = portrait

# Android API
android.api = 33
android.minapi = 21

# Архитектуры (можно выбрать одну для уменьшения размера APK)
android.archs = arm64-v8a,armeabi-v7a
```

#### Шаг 4: Первая сборка (Debug) / Step 4: First Build (Debug)

```bash
# Очистка предыдущих сборок (если были)
buildozer android clean

# Запуск сборки отладочной версии
buildozer -v android debug

# Флаг -v включает подробный вывод (verbose mode)
```

**Важно:** 
- Первая сборка займет 30-90 минут
- Будут скачаны Android SDK, NDK (≈5-7 GB)
- Требуется стабильное интернет-соединение

#### Шаг 5: Мониторинг процесса сборки / Step 5: Monitor Build Process

Процесс сборки включает несколько этапов:

1. ✓ Установка Android SDK
2. ✓ Установка Android NDK
3. ✓ Загрузка Python for Android (p4a)
4. ✓ Сборка зависимостей (kivy, sympy)
5. ✓ Компиляция приложения
6. ✓ Создание APK файла

Следите за выводом в терминале. Если процесс останавливается, проверьте сообщения об ошибках.

#### Шаг 6: Поиск собранного APK / Step 6: Locate the Built APK

После успешной сборки:

```bash
# APK файл будет в директории bin/
ls -lh bin/

# Пример имени файла:
# calclog-1.0-arm64-v8a-debug.apk
# calclog-1.0-armeabi-v7a-debug.apk
```

### Установка APK на устройство / Installing APK on Device

#### Метод 1: Через ADB (Android Debug Bridge) / Method 1: Via ADB

```bash
# Установка ADB (если не установлен)
sudo apt install -y android-tools-adb android-tools-fastboot

# Включите "Отладку по USB" на Android устройстве
# Settings -> Developer Options -> USB Debugging

# Подключите устройство через USB

# Проверка подключения
adb devices

# Установка APK
adb install bin/calclog-1.0-arm64-v8a-debug.apk

# Или используйте Buildozer для установки и запуска
buildozer android deploy run
```

#### Метод 2: Копирование файла / Method 2: File Transfer

1. Скопируйте APK файл из `bin/` на устройство
2. Откройте файловый менеджер на Android
3. Найдите APK файл
4. Нажмите на него для установки
5. Разрешите установку из неизвестных источников (если требуется)

### Сборка Release версии / Building Release Version

Для публикации в Google Play требуется подписанная версия:

#### Шаг 1: Создание ключа подписи / Step 1: Create Signing Key

```bash
# Создание keystore
keytool -genkey -v -keystore calclog-release-key.keystore -alias calclog -keyalg RSA -keysize 2048 -validity 10000

# Сохраните пароль в безопасном месте!
```

#### Шаг 2: Настройка buildozer.spec для Release / Step 2: Configure for Release

Добавьте в `buildozer.spec`:

```ini
[app]
# ... другие настройки ...

# Подпись APK
android.release_artifact = aab
```

#### Шаг 3: Сборка Release APK / Step 3: Build Release APK

```bash
buildozer android release
```

#### Шаг 4: Подписание APK вручную / Step 4: Manual APK Signing

Если требуется подписать вручную:

```bash
# Выравнивание APK
zipalign -v -p 4 bin/calclog-1.0-release-unsigned.apk bin/calclog-1.0-release-unsigned-aligned.apk

# Подписание APK
apksigner sign --ks calclog-release-key.keystore --out bin/calclog-1.0-release-signed.apk bin/calclog-1.0-release-unsigned-aligned.apk

# Проверка подписи
apksigner verify bin/calclog-1.0-release-signed.apk
```

### Оптимизация и настройка / Optimization and Configuration

#### Уменьшение размера APK / Reducing APK Size

1. **Выбор одной архитектуры:**
```ini
# Только для современных устройств (64-bit)
android.archs = arm64-v8a
```

2. **Удаление неиспользуемых зависимостей:**
Проверьте `requirements.txt` и оставьте только необходимые пакеты.

3. **Использование ProGuard (минификация):**
```ini
android.gradle_dependencies = com.android.tools.build:gradle:7.0.0
```

#### Добавление разрешений / Adding Permissions

Если приложению нужен доступ к интернету или другим ресурсам:

```ini
[app]
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
```

#### Изменение иконки и заставки / Changing Icon and Splash Screen

1. Создайте `icon.png` (512x512 пикселей)
2. Создайте `presplash.png` (желательно 1280x720)
3. Разместите в директории проекта
4. Укажите в `buildozer.spec`:

```ini
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png
```

### Устранение проблем / Troubleshooting

#### Ошибка: "Command failed: ..."

**Решение:**
```bash
# Очистите кэш и пересоберите
buildozer android clean
rm -rf .buildozer
buildozer -v android debug
```

#### Ошибка: "java.lang.OutOfMemoryError"

**Решение:**
Увеличьте память для Gradle в `~/.gradle/gradle.properties`:
```properties
org.gradle.jvmargs=-Xmx4096m -XX:MaxPermSize=1024m
```

#### Ошибка: "SDK location not found"

**Решение:**
```bash
export ANDROID_SDK_ROOT=$HOME/.buildozer/android/platform/android-sdk
export ANDROID_HOME=$ANDROID_SDK_ROOT
```

#### Ошибка при импорте sympy на Android

**Решение:**
Sympy может требовать больше памяти. Оптимизируйте импорты в `main.py`:
```python
# Импортируйте только необходимые функции
from sympy import symbols, solve, Eq
# вместо
# from sympy import *
```

#### APK не устанавливается на устройстве

**Решение:**
1. Проверьте версию Android (минимум 5.0 / API 21)
2. Включите установку из неизвестных источников
3. Проверьте архитектуру процессора устройства
4. Пересоберите с правильной архитектурой

### Дополнительные ресурсы / Additional Resources

- [Buildozer Documentation](https://buildozer.readthedocs.io/)
- [Kivy Documentation](https://kivy.org/doc/stable/)
- [Python for Android](https://python-for-android.readthedocs.io/)
- [Android Developer Guide](https://developer.android.com/)

### Тестирование на эмуляторе / Testing on Emulator

#### Установка Android Studio для эмулятора

1. Скачайте Android Studio
2. Установите эмулятор через AVD Manager
3. Запустите эмулятор
4. Установите APK через drag-and-drop

### Обновление приложения / Updating the Application

```bash
# 1. Внесите изменения в код
# 2. Увеличьте версию в buildozer.spec
version = 1.1

# 3. Очистите старую сборку
buildozer android clean

# 4. Пересоберите
buildozer android debug

# 5. Установите на устройство
adb install -r bin/calclog-1.1-arm64-v8a-debug.apk
```

### Публикация в Google Play / Publishing to Google Play

1. Создайте аккаунт разработчика Google Play (единоразовая оплата $25)
2. Соберите подписанный AAB файл (Android App Bundle):
```bash
buildozer android release
```
3. Загрузите AAB в Google Play Console
4. Заполните описание, скриншоты, иконку
5. Пройдите процесс проверки Google

---

**Успешной сборки! / Happy Building!**
