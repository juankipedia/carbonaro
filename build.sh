PYTHON="python3"
COMPILER="carbonaro.py"
CC="gcc"

function comp {
	BN=$(basename -s .carb $1)
	TTOUTPUT=$(${PYTHON} ${COMPILER} $1 2>&1)
	if [ $? -ne 0 ]; then
		echo "${TTOUTPUT}"
	else
		mv out.c output/${BN}.c
		CCOUTPUT=$(${CC} -o output/${BN} output/${BN}.c)
		if [ $? -ne 0 ]; then
			echo "${CCOUTPUT}"
		else
			echo "${TTOUTPUT}"
		fi
	fi
}

if [ $# -eq 0 ]; then
	for i in $(ls examples/*.carb); do
		comp $i
	done
else
	comp $1
fi
