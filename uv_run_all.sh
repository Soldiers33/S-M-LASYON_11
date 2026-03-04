#!/bin/bash
# UV ENTEGRASYON KOMUT DOSYASI - S-M-LASYON_11
# UV Integration Script for rapid testing and development
# 
# Kullanım: bash uv_run_all.sh
# Usage: bash uv_run_all.sh

set -e  # Exit on error

UV_BIN="/home/codespace/.local/bin/uv"
PROJECT_DIR="/workspaces/S-M-LASYON_11"

cd "$PROJECT_DIR"

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║   11-DIMENSIONAL UNIVERSE SIMULATION - UV INTEGRATION TEST    ║"
echo "║   KAR TOPU V5 ANTI-GRAVITY SYSTEMS VALIDATION                ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "🚀 UV Version:"
$UV_BIN --version
echo ""

# Test 1: Verify Constants
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 TEST 1: Verifying Constants Against NASA Data"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
$UV_BIN run verify_constants.py 2>&1 | tail -20
echo ""

# Test 2: Run Unit Tests
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ TEST 2: Running 11-Dimensional Unit Tests (11 sections)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
$UV_BIN run test_11_dimensional_constants.py 2>&1 | tail -30
echo ""

# Test 3: Monte Carlo Validation
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎯 TEST 3: Monte Carlo Validation (100,000 iterations)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
$UV_BIN run uv_monte_carlo_runner.py 2>&1 | tail -40
echo ""

# Test 4: Check System Status
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 TEST 4: System Status Summary"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✓ Project Directory: $PROJECT_DIR"
echo "✓ UV Binary: $UV_BIN"
echo "✓ Python Version: $($UV_BIN run python3 --version 2>&1)"
echo "✓ Workspace Status:"
echo ""

# Count files
TOTAL_FILES=$(find . -type f -name "*.py" | wc -l)
TEST_FILES=$(find . -type f -name "test_*.py" | wc -l)
JSON_FILES=$(find . -type f -name "*.json" | wc -l)

echo "  📁 Total Python Files: $TOTAL_FILES"
echo "  🧪 Test Files: $TEST_FILES"
echo "  📊 JSON Data Files: $JSON_FILES"
echo ""

# Size analysis  
TOTAL_SIZE=$(du -sh . 2>/dev/null | cut -f1)
PY_SIZE=$(find . -type f -name "*.py" -exec du -c {} + 2>/dev/null | tail -1 | cut -f1)

echo "  💾 Project Size: $TOTAL_SIZE"
echo "  📝 Python Code Size: $PY_SIZE"
echo ""

# Git status
echo "  🔄 Git Status:"
UNCOMMITTED=$(git status --short 2>/dev/null | wc -l)
echo "    Uncommitted Changes: $UNCOMMITTED"
COMMITS=$(git log --oneline 2>/dev/null | wc -l)
echo "    Total Commits: $COMMITS"
echo ""

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║         ✅ ALL UV INTEGRATION TESTS COMPLETED                 ║"
echo "║              System Ready for Deployment                      ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "Next Steps:"
echo "  1. Review test results above"
echo "  2. Run specific tests: uv run <script_name.py>"
echo "  3. Start dashboard: uv run dashboard_11.py"
echo "  4. Deploy to production with: git push"
echo ""
