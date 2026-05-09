# untuk membuat workload
import random

# untuk menghitung execution time
import time

# untuk visualisasi grafik distribusi
import matplotlib.pyplot as plt

# DYNAMIC DISTRIBUTION SIMULATION
print("=" * 60)
print("        DYNAMIC DISTRIBUTION SIMULATION")
print("                 NRP 045")
print("=" * 60)

# MEMBUAT WORKER
workers = {
    "Worker_A": 0,
    "Worker_B": 0,
    "Worker_C": 0,
    "Worker_D": 0,
    "Worker_E": 0
}

# GENERATE TASK RANDOM
jumlah_task = 35

tasks = [random.randint(1, 12) for _ in range(jumlah_task)]

print("\nGenerated Tasks:")
print(tasks)

# MULAI SIMULASI
start_time = time.time()

print("\n" + "=" * 60)
print("PROCESS DISTRIBUTION")
print("=" * 60)

for index, task in enumerate(tasks, start=1):

    # memilih worker dengan load terkecil
    selected_worker = min(workers, key=workers.get)

    # menambahkan task ke worker
    workers[selected_worker] += task

    print(
        f"Task-{index:02d}"
        f" | Beban: {task:<2}"
        f" | Dikirim ke: {selected_worker}"
        f" | Total Load: {workers[selected_worker]}"
    )

# SELESAI SIMULASI

end_time = time.time()

execution_time = end_time - start_time

# HASIL AKHIR

print("\n" + "=" * 60)
print("FINAL RESULT")
print("=" * 60)

for worker, load in workers.items():
    print(f"{worker:<10} : {load}")

# ANALISIS
max_load = max(workers.values())
min_load = min(workers.values())
average_load = sum(workers.values()) / len(workers)

# estimasi waktu optimal
expected_optimal_time = max_load

# efisiensi distribusi
efficiency = (min_load / max_load) * 100

print("\n" + "=" * 60)
print("PERFORMANCE ANALYSIS")
print("=" * 60)

print(f"Average Load            : {average_load:.2f}")
print(f"Highest Load            : {max_load}")
print(f"Lowest Load             : {min_load}")
print(f"Expected Optimal Time   : {expected_optimal_time}")
print(f"Distribution Efficiency : {efficiency:.2f}%")
print(f"Execution Time          : {execution_time:.6f} seconds")

# MENENTUKAN KONDISI DISTRIBUSI
difference = max_load - min_load

print("\n" + "=" * 60)
print("LOAD STATUS")
print("=" * 60)

if difference <= 10:
    print("Dynamic distribution sudah mendekati optimal")
else:
    print("Distribusi workload masih belum optimal")

# VISUALISASI

plt.figure(figsize=(9, 5))

plt.bar(workers.keys(), workers.values())

plt.axhline(
    average_load,
    linestyle='--',
    label='Average Load'
)

plt.title("Dynamic Distribution Simulation - NRP 045")
plt.xlabel("Workers")
plt.ylabel("Workload")
plt.legend()

plt.show()
