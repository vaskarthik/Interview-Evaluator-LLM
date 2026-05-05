from evaluator import evaluate_answer, compare_prompt_versions
import json


def main():
    print("=== Interview Evaluation Bot ===")

    question = input("Enter interview question:\n")
    answer = input("\nEnter candidate answer:\n")

    # ✅ Input validation
    if not question.strip() or not answer.strip():
        print("❌ Question and Answer cannot be empty")
        return

    version = input("\nSelect prompt version (v1/v2/v3): ").strip().lower()

    # ✅ Validate version
    if version not in ["v1", "v2", "v3"]:
        print("❌ Invalid version. Defaulting to v1")
        version = "v1"

    print("\n⏳ Evaluating answer... please wait\n")

    result = evaluate_answer(question, answer, version)

    print("\n=== Evaluation Result ===")

    # ✅ Handle errors cleanly
    if "error" in result:
        print("❌ Evaluation failed")
        print("\nRaw LLM Output:")
        print(result.get("raw_output", "No output received"))
    else:
        print(json.dumps(result, indent=2))

    compare = input("\nCompare all prompt versions? (y/n): ").strip().lower()

    if compare == 'y':
        print("\n⏳ Comparing prompt versions...\n")

        results = compare_prompt_versions(question, answer)

        for v, res in results.items():
            print(f"\n--- {v.upper()} ---")

            if isinstance(res, dict):
                for temp, output in res.items():
                    print(f"\n[{temp}]")
                    print(json.dumps(output, indent=2))
            else:
                print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()