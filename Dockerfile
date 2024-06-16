# Користи го официјалниот Python image како основа
FROM python:3.10-alpine

# Постави работен директориум во контејнерот
WORKDIR /app

# Копирај го requirements.txt и инсталирај ги зависностите
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копирај ги сите фајлови од тековниот директориум на хостот во работниот директориум на контејнерот
COPY . /app

# Експонирај го портот на кој апликацијата ќе работи (на пример, 8000 за Django)
EXPOSE 8000

# Дефинирај ја командата која ќе ја стартува Django апликацијата
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]