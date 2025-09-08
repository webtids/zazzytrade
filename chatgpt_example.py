import os

try:
    from openai import OpenAI
except ImportError:
    raise SystemExit("The 'openai' package is required. Install it with 'pip install openai'.")


def main() -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("OPENAI_API_KEY is not set. Copy .env.example to .env and add your key.")
        return

    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model="gpt-4o-mini",
        input="Hello from ZazzyTrade!",
    )
    message = response.output[0].content[0].text
    print(message)


if __name__ == "__main__":
    main()
