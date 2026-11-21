#!/bin/bash
# SPDX-FileCopyrightText: 2026 CHAI YI SHAN
# SPDX-License-Identifier: BSD-3-Clause

ng () {
	echo "${1}行目が違うよ"
	res=1
}

res=0

out=$(printf "25 math\n40 python\n25 math\n" | ./studylog)
[ "${out}" = "90" ] || ng "$LINENO"

out=$(printf "15\n35\n" | ./studylog)
[ "${out}" = "50" ] || ng "$LINENO"

out=$(printf "25 math\n40 python\n25 math\n" | ./studylog -p)
[ "${out}" = "3" ] || ng "$LINENO"

out=$(printf "25 math\n40 python\n25 math\n" | ./studylog -s)
expected=$(printf "math 50\npython 40")
[ "${out}" = "${expected}" ] || ng "$LINENO"

out=$(printf "" | ./studylog 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

out=$(printf "abc math\n" | ./studylog 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

out=$(printf -- "-10 math\n" | ./studylog 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

out=$(printf "25 math\n" | ./studylog -x 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

[ "${res}" = 0 ] && echo "OK"
exit $res
