"""Tiny self-tests for the parts that need no browser or AI:  python test_helpers.py"""
import nl_test as t

def check(name, ok):
    print(("PASS  " if ok else "FAIL  ") + name)
    assert ok

check("parse plain json", t.parse_json('{"action":"wait"}')["action"] == "wait")
check("parse fenced json", t.parse_json('```json\n{"action":"click","id":3}\n```')["id"] == 3)
try:
    t.parse_json("sorry, I cannot"); check("bad json rejected", False)
except ValueError:
    check("bad json rejected", True)

obs = {"fullText": "Welcome back,\n  John   Doe  \nDashboard", "title": "My Account", "url": "https://x.com/dash"}
check("evidence found (case/space insensitive)", t.evidence_ok("welcome back, john doe", obs))
check("made-up evidence rejected", not t.evidence_ok("Payment successful", obs))
check("empty evidence rejected", not t.evidence_ok("", obs))

prompt = t.build_prompt("do x", {"url": "u", "title": "t", "fullText": "hello", "elements": [{"id": 1, "tag": "a"}]}, [])
check("prompt contains test case and element", "do x" in prompt and '"id": 1' in prompt)
print("\nall helper tests passed")
