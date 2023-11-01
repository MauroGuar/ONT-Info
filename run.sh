#!/bin/sh

BLACK='\033[0;30m'
RED='\033[0;31m'
ORANJE='\e[38;5;208m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[0;37m'

BG_BLACK='\033[0;40m'
BG_RED='\033[0;41m'
BG_GREEN='\033[0;42m'
BG_YELLOW='\033[0;43m'
BG_BLUE='\033[0;44m'
BG_MAGENTA='\033[0;45m'
BG_CYAN='\033[0;46m'
BG_WHITE='\033[0;47m'

BOLD='\033[1m'
UNDERLINE='\033[4m'
BLINK='\033[5m'

NC='\033[0m'

echo "${ORANJE}"
echo "H4sIAAAAAAAAA4WRQRLAIAgD77wi5174/++qGCTVjnpgkCTbqQB4xkE/0mAqOZPp7gGEZL33fkJo
dTatjHkrpI7p18P4oCbJwC97mdgICSu2PKILyb75XiJzxorH549r5AcbmQu2PHwErNi81XNF5oKd
ntKVZNSJoRKzMzY9ogvJuG8uO3cuy3cI1jeP6kWyF+Y1Bs64AgAA" | base64 -d | gunzip
# cat your_ascii_art.txt | gzip | base64 # to generate the compressed code above
echo "${NC}\n"

current_dir="$(pwd)"
repo_dir="/ONT-Info"
if [ -z "${current_dir##*$repo_dir}" ] && [ -d .git ]; then
  :
else
  echo "${YELLOW}-> ${RED}YOU ARE NOT IN THE REPOSITORY${NC}\n"
  echo "${YELLOW}-> ${CYAN}Use the command ${BG_GREEN}git clone https://github.com/MauroGuar/ONT-Info.git && cd ONT-Info${NC}"
  exit 1
fi

docker_bin=$(which docker)
if [ -z "$docker_bin" ]; then
  echo "${YELLOW}-> ${RED}DOCKER IS NOT INSTALLED\n"
  echo "${YELLOW}-> ${CYAN}To install Docker, visit https://docs.docker.com/engine/install/\n"
  exit 1
fi

if [ "$(id -u)" != "0" ]; then
  if ! groups | grep -q "\bdocker\b"; then
    if sudo usermod -aG docker $USER; then
      echo "${YELLOW}-> ${CYAN}User has been added to the docker group.${NC}\n"
      echo "${YELLOW}-> ${CYAN}Running '${YELLOW}newgrp docker${CYAN}' to apply group changes...${NC}\n"
      newgrp docker
    else
      echo "${YELLOW}-> ${RED}Failed to add the user to the docker group.${NC}\n"
    fi
  fi
fi

env_file="./app/.env"
if [ ! -f "$env_file" ]; then
  echo "${MAGENTA}> ${CYAN}Enter the OLT SSH username:${NC} \c"
  read olt_username
  echo "\n${MAGENTA}> ${CYAN}Enter the OLT SSH password:${NC} \c"
  stty -echo
  read olt_password
  stty echo
  echo "\n${MAGENTA}> ${CYAN}Enter the flask session secret key:${NC} \c"
  stty -echo
  read flask_session_secret_key
  stty echo
  cp ./app/.env.example $env_file
  sed -i "s/OLT_USERNAME=/&$olt_username/" "$env_file"
  sed -i "s/OLT_PASSWORD=/&$olt_password/" "$env_file"
  sed -i "s/FLASK_SESSION_SECRET_KEY=/&$flask_session_secret_key/" "$env_file"
  echo "\n${YELLOW}-> ${CYAN}Configuration of the .env file completed.\n"
fi

echo "${YELLOW}-> ${CYAN}Running Docker Compose in detached mode\n."
docker compose up --build -d
echo "\n${YELLOW}-> ${GREEN}Installation has been successfully completed.${NC}\n"