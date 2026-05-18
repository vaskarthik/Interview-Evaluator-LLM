import json


def parse_evaluation_output(
    raw_output: str
):
    """
    Parse and validate evaluation JSON output.
    """

    try:

        parsed = json.loads(raw_output)

        validated_output = {
            "score": parsed.get("score"),
            "strengths": parsed.get("strengths", []),
            "weaknesses": parsed.get("weaknesses", []),
            "improvements": parsed.get("improvements", []),
            "final_feedback": parsed.get(
                "final_feedback",
                ""
            ),
        }

        return validated_output

    except Exception as error:

        return {
            "score": None,
            "strengths": [],
            "weaknesses": [],
            "improvements": [],
            "final_feedback": f"Parser Error: {str(error)}",
            "raw_output": raw_output,
        }