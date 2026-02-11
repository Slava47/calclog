# Калькулятор Уравнений / Equation Calculator

Калькулятор для решения логарифмических, обычных и нелинейных уравнений с подробным пошаговым решением.

Calculator for solving logarithmic, regular, and nonlinear equations with detailed step-by-step solutions.

## Возможности / Features

- Решение линейных уравнений / Solving linear equations
- Решение квадратичных и полиномиальных уравнений / Solving quadratic and polynomial equations
- Решение логарифмических уравнений / Solving logarithmic equations
- Решение экспоненциальных уравнений / Solving exponential equations
- Решение тригонометрических уравнений / Solving trigonometric equations
- Подробное пошаговое решение / Detailed step-by-step solution
- Проверка решений / Solution verification
- Красивый графический интерфейс / Beautiful graphical interface
- Поддержка Android / Android support

## Примеры уравнений / Example Equations

- Линейные: `2*x + 5 = 11`
- Квадратичные: `x**2 - 4 = 0`
- Кубические: `x**3 - 2*x**2 + x = 0`
- Логарифмические: `log(x) + 2 = 5`
- Логарифм по основанию: `log(x, 2) = 3`
- Экспоненциальные: `exp(x) - 5 = 0`
- Тригонометрические: `sin(x) = 0.5`

## Установка и запуск на компьютере / Installation and Running on PC

### Требования / Requirements

- Python 3.8 или выше / Python 3.8 or higher
- pip

### Шаги установки / Installation Steps

1. Клонируйте репозиторий / Clone the repository:
```bash
git clone https://github.com/Slava47/calclog.git
cd calclog
```

2. Установите зависимости / Install dependencies:
```bash
pip install -r requirements.txt
```

3. Запустите приложение / Run the application:
```bash
python main.py
```

## Сборка для Android с помощью Buildozer / Building for Android with Buildozer

### Требования для сборки / Build Requirements

- Linux (Ubuntu 20.04 или выше рекомендуется) / Linux (Ubuntu 20.04 or higher recommended)
- Python 3.8+
- Java JDK 17
- Android SDK и NDK (будут установлены автоматически Buildozer)

### Подробная инструкция по сборке / Detailed Build Instructions

#### 1. Установка зависимостей системы / System Dependencies Installation

На Ubuntu/Debian:
```bash
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
```

Для 64-битных систем также установите / For 64-bit systems also install:
```bash
sudo apt install -y build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev zlib1g-dev libssl-dev openssl libgdbm-dev libgdbm-compat-dev liblzma-dev libreadline-dev libncursesw5-dev libffi-dev uuid-dev
```

#### 2. Установка Buildozer / Buildozer Installation

```bash
pip install --upgrade buildozer
pip install --upgrade cython
```

#### 3. Установка Android SDK (если еще не установлен) / Android SDK Installation

Buildozer автоматически скачает Android SDK и NDK при первой сборке.
Buildozer will automatically download Android SDK and NDK on first build.

Убедитесь, что у вас достаточно места на диске (минимум 10 ГБ) / Make sure you have enough disk space (minimum 10 GB).

#### 4. Первая сборка APK / First APK Build

В директории проекта выполните / In the project directory, run:

```bash
# Для отладочной сборки / For debug build
buildozer android debug

# Для релизной сборки / For release build
buildozer android release
```

**Важно:** Первая сборка займет много времени (30-60 минут), так как будут скачаны все необходимые компоненты.

**Important:** The first build will take a long time (30-60 minutes) as all necessary components will be downloaded.

#### 5. Установка APK на устройство / Installing APK on Device

После успешной сборки APK-файл будет находиться в директории `bin/`:

```bash
# Найти собранный APK / Find the built APK
ls -lh bin/*.apk

# Установить на подключенное устройство через ADB / Install on connected device via ADB
buildozer android deploy run
```

Или скопируйте APK-файл на устройство вручную и установите.

Or copy the APK file to your device manually and install it.

### Решение проблем при сборке / Build Troubleshooting

#### Проблема: Ошибка при компиляции / Issue: Compilation Error

**Решение:** Убедитесь, что установлены все системные зависимости.

**Solution:** Make sure all system dependencies are installed.

```bash
sudo apt install -y build-essential git python3 python3-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev
```

#### Проблема: Недостаточно памяти / Issue: Out of Memory

**Решение:** Увеличьте swap-файл или используйте компьютер с большим объемом RAM.

**Solution:** Increase swap file or use a computer with more RAM.

#### Проблема: Не находит Java / Issue: Java Not Found

**Решение:** Установите JDK 17 и настройте переменную окружения JAVA_HOME.

**Solution:** Install JDK 17 and set JAVA_HOME environment variable.

```bash
sudo apt install openjdk-17-jdk
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
```

#### Проблема: Buildozer не может скачать компоненты / Issue: Buildozer Cannot Download Components

**Решение:** Проверьте подключение к интернету и настройки прокси.

**Solution:** Check internet connection and proxy settings.

### Настройка приложения / Application Configuration

Вы можете настроить параметры приложения в файле `buildozer.spec`:

- `title`: Название приложения / Application title
- `package.name`: Имя пакета / Package name
- `package.domain`: Домен пакета / Package domain
- `version`: Версия приложения / Application version
- `orientation`: Ориентация экрана (portrait/landscape) / Screen orientation
- `android.permissions`: Разрешения Android / Android permissions

### Обновление APK / Updating APK

1. Внесите изменения в код / Make changes to the code
2. Увеличьте версию в `buildozer.spec` / Increment version in `buildozer.spec`
3. Пересоберите приложение / Rebuild the application:
```bash
buildozer android clean
buildozer android debug
```

## Использование / Usage

1. Введите уравнение в поле ввода / Enter equation in the input field
2. Используйте `x` как переменную / Use `x` as the variable
3. Нажмите "Решить" для получения решения / Click "Solve" to get the solution
4. Просмотрите пошаговое решение / Review the step-by-step solution

### Поддерживаемые функции / Supported Functions

- `log(x)` - натуральный логарифм / natural logarithm (ln)
- `log(x, base)` - логарифм по основанию / logarithm with base
- `exp(x)` - экспонента / exponential
- `sin(x)`, `cos(x)`, `tan(x)` - тригонометрические функции / trigonometric functions
- `sqrt(x)` - квадратный корень / square root
- `x**2` - возведение в степень / power

## Лицензия / License

MIT License

## Автор / Author

Slava47

## Вклад / Contributing

Приветствуются pull requests и issues!

Pull requests and issues are welcome!
