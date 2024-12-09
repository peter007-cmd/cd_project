import os
import random

OUTPUT_FOLDER = "Generated_Codes"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def generate_constant_program():
    return """
#include <stdio.h>

int main() {
    int x = 10;
    printf("Constant program with value: %d\\n", x);
    return 0;
}
"""

def generate_linear_program():
    n = random.randint(10, 50)
    return f"""
#include <stdio.h>

int main() {{
    int sum = 0;
    for (int i = 0; i < {n}; i++) {{
        sum += i;
    }}
    printf("Sum of first {n} numbers: %d\\n", sum);
    return 0;
}}
"""

def generate_quadratic_program():
    n = random.randint(5, 20)
    return f"""
#include <stdio.h>

int main() {{
    int sum = 0;
    for (int i = 0; i < {n}; i++) {{
        for (int j = 0; j < {n}; j++) {{
            sum += i + j;
        }}
    }}
    printf("Sum of pairs in {n}x{n} grid: %d\\n", sum);
    return 0;
}}
"""

def generate_exponential_program():
    n = random.randint(3, 6)
    return f"""
#include <stdio.h>

int fib(int n) {{
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}}

int main() {{
    int result = fib({n});
    printf("Fibonacci of {n}: %d\\n", result);
    return 0;
}}
"""

def generate_programs(num_programs):
    complexities = ["constant", "linear", "quadratic", "exponential"]
    generators = {
        "constant": generate_constant_program,
        "linear": generate_linear_program,
        "quadratic": generate_quadratic_program,
        "exponential": generate_exponential_program,
    }

    for i in range(num_programs):
        complexity = random.choice(complexities)
        file_name = os.path.join(OUTPUT_FOLDER, f"program_{i+1}_{complexity}.c")
        program_code = generators[complexity]()
        with open(file_name, "w") as f:
            f.write(program_code)
        print(f"Generated: {file_name}")

# Generate 10 random programs
generate_programs(10)
