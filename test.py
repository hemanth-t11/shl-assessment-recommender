from retriever import retrieve

query = "Java Backend Developer"

results = retrieve(query)

for i, r in enumerate(results):

    print("=" * 50)

    print(i + 1)

    print(r["name"])

    print(r["link"])

    print(r["description"][:200])