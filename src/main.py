from evaluator import evaluate_answer, compare_prompt_versions
import json

def main():
    print("=== Interview Evaluation Bot ===")

    question = input("Enter interview question:\n")
    answer = input("\nEnter candidate answer:\n")

    version = input("\nSelect prompt version (v1/v2/v3): ").strip()

    result = evaluate_answer(question, answer, version)

    print("\n=== Evaluation Result ===")
    print(json.dumps(result, indent=2))

    compare = input("\nCompare all prompt versions? (y/n): ")

    if compare.lower() == 'y':
        results = compare_prompt_versions(question, answer)
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()