# OpenFaaS Benchmarking Functions

This repository contains OpenFaaS functions designed for benchmarking purposes. Each function is focused on measuring different aspects of performance.

## Functions Overview

1. **cpu.py**
   - This function performs CPU-intensive operations. It is suitable for benchmarking the CPU utilization of your OpenFaaS environment.

2. **io.py**
   - The `io.py` function focuses on simulating I/O-intensive tasks. Use this function to benchmark the I/O performance of your OpenFaaS setup.

3. **memory_intensive.py**
   - The `memory_intensive.py` function is designed to test the memory usage of your OpenFaaS platform. It performs memory-intensive operations to assess how well your system handles such workloads.

## Usage

1. Ensure you have OpenFaaS installed and configured in your environment.

2. Deploy the desired function using the OpenFaaS CLI:

    ```bash
    faas-cli deploy -f <file-name.yml>
    ```

3. Invoke the function to initiate the benchmark:

    ```bash
    faas-cli invoke <function-name>
    ```

4. Monitor the performance metrics of your OpenFaaS platform during the benchmark to gather insights.

## Considerations

- Adjust the function configurations and resource limits based on your benchmarking requirements.
- Analyze the obtained metrics and adjust your OpenFaaS environment accordingly for optimal performance.

