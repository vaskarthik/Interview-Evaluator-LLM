from langchain_core.prompts import PromptTemplate

evaluation_prompt = PromptTemplate(
    input_variables=["final_prompt"],
    template="{final_prompt}"
)