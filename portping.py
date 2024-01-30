#!/usr/bin/env python3
import argparse
import socket
import time

def check_connection(host, port=80, count=5):
    min_time = float('inf')
    max_time = 0.0
    total_time = 0.0
    successful_attempts = 0

    for i in range(1, count + 1):
        start_time = time.monotonic()  # start timing
        connection_successful = False  # Track connection success

        try:
            # Try to create a socket connection to the host and port
            with socket.create_connection((host, port), timeout=1) as conn:
                connection_successful = True  # Connection was successful
        except (socket.timeout, socket.error) as e:
            print(f"Attempt {i}: Failed to connect to {host}:{port}")

        end_time = time.monotonic()  # stop timing
        elapsed_time = end_time - start_time  # calculate elapsed time
        elapsed_time_ms = elapsed_time * 1000  # convert to milliseconds

        # Only considering successful attempts for min/max/avg calculations
        if connection_successful:
            successful_attempts += 1
            total_time += elapsed_time_ms
            min_time = min(min_time, elapsed_time_ms)
            max_time = max(max_time, elapsed_time_ms)
            print(f"Attempt {i}: Time to connect to {host}:{port} is {elapsed_time_ms:.2f}ms")

        # If the attempt took less than 1 second, wait for the remainder of the time
        if i < count and elapsed_time < 1:
            time.sleep(1 - elapsed_time)

    # Summary calculation
    if successful_attempts > 0:
        average_time = total_time / successful_attempts
    else:
        average_time = min_time = max_time = 0

    failed_percentage = ((count - successful_attempts) / count) * 100 if count > 0 else 0

    # Summary output
    print(f"\n--- {host} port {port} connection statistics ---")
    print(f"{count} connections, {successful_attempts} successful, {failed_percentage:.0f}% failed, time {total_time:.2f} ms")
    print(f"rtt min/avg/max = {min_time:.2f}/{average_time:.2f}/{max_time:.2f} ms")

if __name__ == "__main__":
    # Define argument parser to parse command line arguments
    parser = argparse.ArgumentParser(description="Ping a port to check the connection.")
    parser.add_argument("host", type=str, help="Hostname or IP to ping")
    parser.add_argument("-p", "--port", default=80, type=int, help="Port number to ping (default: 80)")
    parser.add_argument("-c", "--count", default=5, type=int, help="Number of pings to send (default: 5)")

    # Parse the arguments
    args = parser.parse_args()

    # Run the check_connection function with provided arguments
    check_connection(args.host, args.port, args.count)
