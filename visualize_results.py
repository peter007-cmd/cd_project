import pandas as pd
import matplotlib.pyplot as plt

# Load compile time data
data = pd.read_csv("compile_times.csv")

data["CompileTime(s)"] = pd.to_numeric(data["CompileTime(s)"], errors="coerce")
data = data.dropna(subset=["CompileTime(s)"])

complexities = ["constant", "linear", "quadratic", "exponential"]

for complexity in complexities:
    filtered_data = data[data["Program"].str.contains(complexity)]
    
    if filtered_data.empty:
        print(f"No data for {complexity} complexity. Skipping...")
        continue
    
    pivot_data = filtered_data.pivot(index="Program", columns="Compiler", values="CompileTime(s)")
    
    pivot_data = pivot_data.sort_index()

    plt.figure(figsize=(10, 6))
    for compiler in pivot_data.columns:
        plt.plot(pivot_data.index, pivot_data[compiler], marker="o", label=compiler)

    plt.title(f"Compiler Comparison - {complexity.capitalize()} Time Complexity")
    plt.xlabel("Programs")
    plt.ylabel("Average Compile Time (seconds)")
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()

    # Save the plot
    output_file = f"compile_times_{complexity}_line.png"
    plt.savefig(output_file)
    plt.close()
    
    print(f"Saved line chart for {complexity} complexity as {output_file}")

print("All line charts generated successfully.")
