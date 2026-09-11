from converter import json_to_env

print("🔄 JSON to ENV Converter")
print("=" * 35)

data = input("Paste JSON: ").strip()

try:
    result = json_to_env(data)

    print("\n📄 Generated .env:\n")
    print(result)

except ValueError:
    print("❌ Invalid JSON.")
