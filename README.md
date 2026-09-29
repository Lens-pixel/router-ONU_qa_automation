# router-ONU_qa_automation
Python-based automated smoke testing framework for validating hardware interfaces, network connectivity, and Web Admin GUI availability on routers and switches.

 Features Tested
- **Gigabit Port Link Validation:** Verifies 1Gbps interface state.
- **Latency & ICMP Check:** Measures average RTT and flags packet loss.
- **Web Admin Availability:** Asserts HTTP/HTTPS response code `200 OK`.
- **Automated Logging:** Generates clear CLI pass/fail output.

 Tech Stack
- Python 3.10+
- Pytest
- Requests / Subprocess

 How to Run
```bash
pip install -r requirements.txt
pytest tests/ -v
