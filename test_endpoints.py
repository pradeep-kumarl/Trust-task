from starlette.testclient import TestClient
from app.main import app

def test_app():
    client = TestClient(app)

    # 1. Test Health
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
    print("[PASS] /health")

    # 2. Test Tasks API
    r = client.get("/api/tasks")
    assert r.status_code == 200
    tasks = r.json()
    assert len(tasks) > 0
    print(f"[PASS] /api/tasks (returned {len(tasks)} tasks)")

    # 3. Test Filtered Tasks
    r = client.get("/api/tasks?min_hourly=20")
    assert r.status_code == 200
    filtered = r.json()
    assert all(t["hourly_rate_usd"] >= 20 for t in filtered)
    print(f"[PASS] /api/tasks?min_hourly=20 (returned {len(filtered)} high-paying tasks)")

    # 4. Test Platforms API
    r = client.get("/api/platforms")
    assert r.status_code == 200
    platforms = r.json()
    assert len(platforms) > 0
    print(f"[PASS] /api/platforms (returned {len(platforms)} platforms)")

    # 5. Test Stats API
    r = client.get("/api/stats")
    assert r.status_code == 200
    stats = r.json()
    assert stats["active_genuine_tasks"] > 0
    print(f"[PASS] /api/stats: {stats}")

    # 6. Test Scam Checker API (Scam text)
    scam_payload = {"text_content": "Pay $20 registration fee to get access to $500 surveys!"}
    r = client.post("/api/check-url", json=scam_payload)
    assert r.status_code == 200
    res = r.json()
    assert not res["is_safe"]
    assert "Demands upfront payment" in res["detected_red_flags"][0]
    print(f"[PASS] /api/check-url (Scam detected: score={res['score']}, verdict={res['verdict']})")

    # 7. Test Scam Checker API (Genuine platform)
    safe_payload = {"url": "https://usertesting.com", "text_content": "User testing platform"}
    r = client.post("/api/check-url", json=safe_payload)
    assert r.status_code == 200
    res = r.json()
    assert res["is_safe"]
    print(f"[PASS] /api/check-url (Verified safe: score={res['score']}, verdict={res['verdict']})")

    # 8. Test Frontend Static Index
    r = client.get("/")
    assert r.status_code == 200
    assert "TrustTask" in r.text
    print("[PASS] Frontend / (HTML dashboard served)")

    print("\nALL 8 TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    test_app()
