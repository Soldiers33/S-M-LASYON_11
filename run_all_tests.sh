for f in test_*.py; do
    echo "Running $f"
    python3 $f || echo "$f failed"
done
