import time

def run_benchmark():
    print("Starting Thor Digital Twin Latency Benchmark...")
    # Simulating round-trip execution measurement (~1.9s average target)
    latencies = []
    for i in range(5):
        start_time = time.time()
        time.sleep(1.9)  # Simulated network/execution round-trip delay
        duration = time.time() - start_time
        latencies.append(duration)
        print(f"Test {i+1}: Round-trip latency = {duration:.2f}s")
    
    avg_latency = sum(latencies) / len(latencies)
    print(f"\nBenchmark Complete. Average Round-Trip Latency: {avg_latency:.2f}s")

if __name__ == "__main__":
    run_benchmark()
