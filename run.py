import sys
import os
import uvicorn

if __name__ == "__main__":
    # Ensure current directory is on python path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)

    print("=" * 65)
    print("  TrustTask | Genuine Survey & Microtask Intelligence Engine")
    print("=" * 65)
    print("  [+] Server starting on: http://127.0.0.1:8000")
    print("  [+] API Docs available: http://127.0.0.1:8000/docs")
    print("  [+] Press Ctrl+C to terminate.")
    print("=" * 65)

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
