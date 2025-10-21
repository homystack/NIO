FROM python:3.11-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    git \
    openssh-client \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Установка Nix
RUN sh <(curl -L https://nixos.org/nix/install) --no-daemon

# Добавление Nix в PATH
ENV PATH="/root/.nix-profile/bin:$PATH"

# Установка nixos-anywhere и nixos-rebuild
RUN nix-env -iA nixpkgs.nixos-anywhere nixpkgs.nix

# Создание рабочей директории
WORKDIR /app

# Копирование зависимостей
COPY requirements.txt .

# Установка Python зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода оператора
COPY main.py .

# Создание пользователя для безопасности
RUN groupadd -r operator && useradd -r -g operator operator
USER operator

# Запуск оператора
CMD ["python", "main.py"]
