import json, urllib.request, urllib.parse
ENV = r"C:\Users\danie\Documents\Claude\Projects\Social Scheduler\social-layer\.env"
env = {}
for line in open(ENV, encoding="utf-8-sig"):
    if "=" in line and not line.strip().startswith("#"):
        k, v = line.strip().split("=", 1); env[k] = v.strip().strip('"')
base = env["POSTIZ_LOCAL_URL"].rstrip("/") + "/api/public/v1"
H = {"Authorization": env["POSTIZ_API_KEY"]}
for d in ["2026-09-25", "2026-10-02", "2026-10-09"]:
    q = urllib.parse.urlencode({"startDate": d + "T00:00:00Z", "endDate": d + "T23:59:59Z"})
    try:
        r = urllib.request.urlopen(urllib.request.Request(base + "/posts?" + q, headers=H), timeout=60)
        data = json.loads(r.read().decode())
        posts = data.get("posts", data) if isinstance(data, dict) else data
        print(d, "->", len(posts), "posts")
        for p in posts:
            integ = p.get("integration", {}) or {}
            print("  ", p.get("id"), p.get("publishDate"), p.get("state") or p.get("status"),
                  integ.get("providerIdentifier"), integ.get("name"),
                  (p.get("content") or "")[:70].replace("\n", " "))
    except Exception as e:
        print(d, "ERR", e)
