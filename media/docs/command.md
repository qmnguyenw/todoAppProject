Write down all shell command before execution

# Visual Studio Code

Install these extensions

- Visual Studio Keymap
- Debugger for Chrome
- TSLint 
(for front end development)
- Python
- Visual Studio Intellicode
(for back end development)

# PostgreSQL

Install PostgreSQL 11 on Linux
Install pgAdmin4

# Chrome

# Fcitx Unikey

# Anaconda (Python)
Install Anaconda
Learn Anaconda environment 

# Bash shell (Linux)

# Git
Create and update SSH key
Clone 2 project frontend and backend

# NPM
Install latest LTS npm and nodejs

# Change date/time of OS


sudo apt update

# nodejs - npm
sudo apt-get install curl
curl -sL https://deb.nodesource.com/setup_13.x | sudo -E bash -
sudo apt-get install nodejs
node -v
npm -v

# Download deb file VSCode - Chrome
sudo dpkg -i Downloads/code_1.41.0-1576089540_amd64.deb 
sudo dpkg -i Downloads/google-chrome-stable_current_amd64.deb 

# postgresql
sudo apt-get install wget ca-certificates
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
sudo apt-get install postgresql postgresql-contrib

sudo su - postgres
psql
postgres-# \conninfo
postgres-# \q

# pgAdmin4
sudo apt-get install pgadmin4 pgadmin4-apache2
\\if error 
    E: Package 'pgadmin4' has no installation candidate
    E: Unable to locate package pgadmin4-apache2
sudo nano /etc/apt/sources.list.d/pgdg.list
deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main
sudo wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt update
sudo apt install pgadmin4 pgadmin4-apache2

username: postgres@localhost
pass: 1

# anaconda
https://www.anaconda.com/distribution/
cd /tmp
curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
sha256sum Anaconda3-2019.03-Linux-x86_64.sh
bash Anaconda3-2019.03-Linux-x86_64.sh
yes
yes
source ~/.bashrc
conda list
conda create --name my_env python=3
conda activate my_env

# fcitx unikey
sudo apt-get install fcitx-unikey
im-config -n fcitx

# git
cd ~/.ssh
ssh-keygen -o
cat ~/.ssh/id_rsa.pub

# postman, netstat
sudo apt install net-tools   
netstat -tulpn | grep LISTEN 
htop
kill -9 <name process if duplicate address>

tar -xzf Postman-linux-x64-7.14.0.tar.gz 
cd Postman/
ls
ls -all
./Postman



# EX

pip install pipenv
npm install -g @angular/cli
conda install -c conda-forge marshmallow-sqlalchemy
conda install -c anaconda psycopg2
conda install -c anaconda cryptography
conda install -c conda-forge flask-marshmallow
conda install -c anaconda flask-cors
conda config --add channels conda-forge
conda install python-jose-cryptodome
conda search python-jose-cryptodome --channel conda-forge
conda install -c conda-forge alembic 

# Git Note
 when up code to my branch
$ cd myproject
$ git checkout myBranch
$ git push -u origin myBranch
In some cases -u showed as invalid argument, so use this
$ git push origin <local name>


# Angular
ng serve
ng g component components/user -> create user things ....

cat /proc/cpuinfo
watch nvidia-smi
apt search nvidia | grep installed
apt search nvidia-driver


# Django
python manage.py makemigrations (polls) - see change in model db / these change store in migration, create migrations for those changes
python manage.py sqlmigrate polls 0001 - generate db in each sql
python manage.py migrate - apply those changes to the database.

superuser admin guest3499

```
python manage.py shell 
from django.contrib.auth.models import User
user=User.objects.create_user('foo', password='bar')
user.is_superuser=True
user.is_staff=True
user.save()
```

# scp
scp -r zmExport ducanh@192.168.0.134:~/
