#!/usr/bin/env bash
# Puja una versió nova al repo (bauram/honest). Ús:
#   bash deploy.sh "missatge del commit"
# Si no poses missatge, en fica un amb la data.
set -e

# assegura que el remot hi és (per si es fa servir en una còpia nova)
git remote get-url origin >/dev/null 2>&1 || git remote add origin git@github.com:bauram/honest.git

MSG="${1:-Actualització web $(date '+%Y-%m-%d %H:%M')}"

git add -A
if git diff --cached --quiet; then
  echo "· No hi ha canvis per pujar."
  exit 0
fi
git commit -m "$MSG"
git push
echo ""
echo "✔ Versió pujada: \"$MSG\""
