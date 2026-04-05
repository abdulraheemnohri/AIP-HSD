import os
import subprocess
import sys

def run_test(command, description):
    print(f"--- RUNNING: {description} ---")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[SUCCESS] {description}")
            return True
        else:
            print(f"[FAILED] {description}")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"[ERROR] {description}: {str(e)}")
        return False

def main():
    print("AIP-HSD // UNIVERSAL TEST RUNNER STARTING...")

    # Define tests
    tests = [
        ("python3 ai_module/orchestrator.py", "AI Orchestration Loop"),
        ("ruby scripts/sentinel_health.rb", "Sentinel Health Diagnostic"),
        ("perl scripts/forensics.pl", "Perl Legacy Forensics"),
        ("python3 ai_module/adversarial_shield.py", "Adversarial AI Defense"),
        ("python3 agents/python/red_team.py", "Autonomous Red Team Simulator")
    ]

    # Setup Python Path
    os.environ['PYTHONPATH'] = f"{os.getcwd()}/backend/python:{os.getcwd()}"

    success_count = 0
    for cmd, desc in tests:
        if run_test(cmd, desc):
            success_count += 1

    print("\n" + "="*40)
    print(f"TOTAL TESTS: {len(tests)}")
    print(f"PASSED: {success_count}")
    print(f"FAILED: {len(tests) - success_count}")
    print("="*40)

    if success_count == len(tests):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
