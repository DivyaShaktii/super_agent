import argparse
from pipelines.research_pipeline import ResearchPipeline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--mode", choices=["react", "graph"], default="graph")
    parser.add_argument("--provider", choices=["openai", "anthropic", "gemini"], default="openai")
    parser.add_argument("--images", action="store_true")
    args = parser.parse_args()

    pipeline = ResearchPipeline(mode=args.mode, provider=args.provider)
    output = pipeline.research(args.query, include_images=args.images)

    print("\n🔍 Answer:")
    print(output["result"])
    if args.images:
        print("\n🖼️ Images:")
        for url in output["images"]:
            print(url)

if __name__ == "__main__":
    main()
