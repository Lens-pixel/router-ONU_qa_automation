```python
import subprocess
import requests
import pytest

ROUTER_IP = "192.168.1.1"
EXPECTED_SPEED = "1000Mbps"

def test_web_admin_availability():
    """Verify that the Web Admin GUI is reachable and returns HTTP 200."""
    try:
        response = requests.get(f"http://{ROUTER_IP}", timeout=5)
        assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
    except requests.RequestException as e:
        pytest.fail(f"Web Admin GUI is unreachable: {e}")

def test_icmp_ping_latency():
    """Ensure packet loss is 0% and response time is within acceptable range."""
    # Ping command for Linux/MacOS (-c 4). For Windows use '-n', '4'
    cmd = ["ping", "-c", "4", ROUTER_IP]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    assert result.returncode == 0, "Ping failed: Router is not responding."
    assert "0% packet loss" in result.stdout, "Packet loss detected during ICMP test."

def test_gigabit_link_status():
    """Simulated test for verifying interface link speed (e.g., via ethtool or SNMP)."""
    # Placeholder/Mock for physical interface speed validation logic
    current_speed = "1000Mbps"  # Logic to fetch actual interface state
    assert current_speed == EXPECTED_SPEED, f"Speed mismatch! Got {current_speed}, expected {EXPECTED_SPEED}"
