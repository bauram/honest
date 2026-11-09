#!/usr/bin/env bash
# Puja la web d'Honest a github.com/bauram/honest i la desplega a Netlify.
#
#   bash deploy.sh "missatge"          → puja a GitHub + desplegament de PROVA
#   bash deploy.sh "missatge" prod     → puja a GitHub + PRODUCCIÓ (honestpg.com)
#
set -euo pipefail

REPO_URL="https://github.com/bauram/honest.git"
BRANCH="main"
SITE_ID="06afaf32-06b9-4100-b554-337f06d5dcd1"   # hiobest / honestpg.com
DIR="dist"
MSG="${1:-Actualitzacio de la web d Honest}"
MODE="${2:-draft}"

cd "$(dirname "$0")"
# genera la web estatica (una URL per pagina) abans de desplegar
python3 build.py || { echo "✗ La build ha fallat"; exit 1; }
[ -f "$DIR/index.html" ] || { echo "✗ No trob ./$DIR/index.html"; exit 1; }

# ---------- 1. GitHub ----------
[ -d .git ] || git init

# lock oblidat d un proces anterior
if [ -f .git/index.lock ] && ! pgrep -x git >/dev/null; then
  rm -f .git/index.lock
  echo "→ Eliminat .git/index.lock antic."
fi

touch .gitignore
grep -qxF '*.zip'     .gitignore || echo '*.zip'     >> .gitignore
grep -qxF '.DS_Store' .gitignore || echo '.DS_Store' >> .gitignore

if git remote | grep -qx origin; then
  git remote set-url origin "$REPO_URL"
else
  git remote add origin "$REPO_URL"
fi

git add -A
git commit -m "$MSG" || echo "→ Res de nou per commitejar."
git branch -M "$BRANCH"
git push -u origin "$BRANCH"
echo "✓ Pujat a $REPO_URL ($BRANCH)"

# ---------- 2. Netlify ----------
if [ "$MODE" = "prod" ]; then
  echo "⚠  Desplegament a PRODUCCIÓ: substituirà honestpg.com."
  read -r -p "   Escriu SI per continuar: " ok
  [ "$ok" = "SI" ] || { echo "Deploy cancel·lat (el codi ja és a GitHub)."; exit 0; }
  npx --yes netlify-cli@latest deploy --site "$SITE_ID" --dir "$DIR" --prod
else
  echo "→ Desplegament de prova (no toca honestpg.com)."
  npx --yes netlify-cli@latest deploy --site "$SITE_ID" --dir "$DIR"
fi
