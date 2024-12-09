#!/bin/bash

OUTPUT_FILE="compile_times.csv"
COMPILERS=("gcc" "clang" "tcc")
PROGRAM_DIR="Generated_Codes"
EXECUTIONS=5 

echo "Program,Compiler,CompileTime(s)" > "$OUTPUT_FILE"

for file in "$PROGRAM_DIR"/*.c; do
    for compiler in "${COMPILERS[@]}"; do
        total_time=0

        for ((i = 1; i <= EXECUTIONS; i++)); do
            start=$(date +%s%N)
            $compiler -o /dev/null "$file"
            end=$(date +%s%N)
            elapsed=$((end - start))
            total_time=$(echo "$total_time + $elapsed" | bc)
        done

        avg_time=$(echo "scale=9; $total_time / ($EXECUTIONS * 1000000000)" | bc)
        echo "$(basename "$file"),$compiler,$avg_time" >> "$OUTPUT_FILE"
    done
done

echo "Compilation times logged in $OUTPUT_FILE."
