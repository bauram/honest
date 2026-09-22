#!/usr/bin/env bash
# Desplega la web d'Honest a Netlify (site "hiobest" → honestpg.com).
#
#   bash deploy-netlify.sh          → desplegament de PROVA (URL temporal, no toca honestpg.com)
#   bash deploy-netlify.sh prod     → desplegament a PRODUCCIÓ (substitueix honestpg.com)
#
set -euo pipefail

SITE_ID="06afaf32-06b9-4100-b554-337f06d5dcd1"   # hiobest / honestpg.com
DIR="web"

cd "$(dirname "$0")"

if [ ! -f "$DIR/index.html" ]; then
  echo "✗ No trob l'index.html dins ./$DIR"; exit 1
fi

if [ "${1:-}" = "prod" ]; then
  echo "⚠  Desplegament a PRODUCCIÓ: això substituirà honestpg.com."
  read -r -p "   Escriu SI per continuar: " ok
  [ "$ok" = "SI" ] || { echo "Cancel·lat."; exit 0; }
  FLAGS="--prod"
else
  echo "→ Desplegament de prova (no toca honestpg.com)."
  FLAGS=""
fi

npx --yes netlify-cli@latest deploy --site "$SITE_ID" --dir "$DIR" $FLAGS
