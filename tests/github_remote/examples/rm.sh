#!/usr/bin/env bash
{ set +x; } 2>/dev/null

cd "${BASH_SOURCE[0]%/*/*/*/*}" || exit
( set -x; python -m github_remote.rm ) || exit
