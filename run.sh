#!/bin/bash

echo ""
# print compressed ascii art
base64 -d <<<"H4sIAAAAAAAAA4WRQRLAIAgD77wi5174/++qGCTVjnpgkCTbqQB4xkE/0mAqOZPp7gGEZL33fkJo
dTatjHkrpI7p18P4oCbJwC97mdgICSu2PKILyb75XiJzxorH549r5AcbmQu2PHwErNi81XNF5oKd
ntKVZNSJoRKzMzY9ogvJuG8uO3cuy3cI1jeP6kWyF+Y1Bs64AgAA" | gunzip
# cat your_ascii_art.txt | gzip | base64  # to generate the compressed code above
echo ""

filetoread="README.md"
stringtofind="ONT-Info"

if [ -f "$filetoread" ]; then
  if ! grep -q "$stringtofind" "$filetoread"; then
    echo "The word '$stringtofind' was not found inside $filetoread. Are you sure you are inside the repo?"
  fi
else
  echo "The file $filetoread does not exist. Are you sure you are inside the repo?"
fi

if ! groups | grep -q "\bdocker\b"; then
  # add user to docker group
  sudo usermod -aG docker $USER
  echo "User has been added to docker group. this will take effect after restarting your session using the following command : exec su -l $USER"
fi

filetowrite="./app/.env"
# if the file exists
if [ -f "$filetowrite" ]; then
  echo "it seems that the .env already exist, skipping .env setup"
else
  # take input from user
  read -p "Insert the OLT ssh username: " olt_username
  read -p "Insert the OLT ssh username's password: " olt_password
  # copy the env file
  cp ./app/.env.example $filetowrite
  #
  sed -i "s/OLT_USERNAME=/&$olt_username/" "$filetowrite"
  sed -i "s/OLT_PASSWORD=/&$olt_password/" "$filetowrite"
  echo ".env setup finished"
fi

echo "running docker compose in detached mode"
sudo docker compose up -d 