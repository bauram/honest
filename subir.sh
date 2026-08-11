#!/usr/bin/env bash
# Sube esta carpeta al repo de GitHub (bauram/honest). Ejecutar: bash subir.sh
set -e
git init
git add .
git commit -m "Honest web"
git branch -M main
git remote add origin git@github.com:bauram/honest.git 2>/dev/null || git remote set-url origin git@github.com:bauram/honest.git
git push -u origin main
echo ""
echo "✔ Subido. Activa GitHub Pages en: Settings → Pages → Branch: main / root"
