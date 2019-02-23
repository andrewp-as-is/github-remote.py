#!/usr/bin/env bash
{ set +x; } 2>/dev/null

( set -x; python -m github_remote.rm ) || exit
