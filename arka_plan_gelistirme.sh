#!/bin/bash
# Autonomous background execution of the simulation

echo "Starting continuous background simulation execution..."
while true; do
    echo "Running simulasyon_11.py at $(date)"
    python3 simulasyon_11.py >> arka_plan_simulasyon_output.log 2>&1
    echo "Sleeping for 60 seconds before next run..."
    sleep 60
done
