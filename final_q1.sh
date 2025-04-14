#!/bin/bash
#iterating through all lines 
while read line; do
	#every iteration is one term
	result_line=$(echo $line)
	while read term; do
		repl="UNKNOWN TEXT"
		#every iteration  checks a row in the ref table
		while read table_row; do
			#when the line is found
			if echo $table_row | grep -E -q "^$term(,[^,]*){2}"; then
				if [ "$(echo $table_row | cut -d"," -f2)" == "text" ]; then
					#repl=$(echo $table_row | cut -d"," -f3 | tr -d "\"")
					repl=$(echo $table_row | cut -d"," -f3 | sed "s/^\"//" | sed "s/\"$//")
				elif [ "$(echo $table_row | cut -d"," -f2)" == "number" ]; then
					repl=$(echo $table_row | cut -d"," -f3)
				elif [ "$(echo $table_row | cut -d"," -f2)" == "formula" ]; then
					repl=$(echo "$table_row" | cut -d"," -f3 | bc)
				fi
				break
			fi
		done <$2
		result_line=$(echo $result_line | sed "s/{:$term:}/$repl/")
	done < <(echo $line | grep -o "{:[^:}]*:}" | sed -E "s/\{:([^:\}]*):\}/\1/")

	#printout the final outcome of the line
	echo $result_line
done <$1
