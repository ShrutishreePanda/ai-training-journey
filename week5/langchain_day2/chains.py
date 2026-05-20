from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda
from schemas import RequirementAnalysis

llm = ChatOllama(model="llama3")

parser = StrOutputParser()

structured_llm = (
    llm
    .with_structured_output(RequirementAnalysis)
    .with_retry(
        stop_after_attempt=3
    )
)

structured_prompt = ChatPromptTemplate.from_template(
    """
    Analyze this software requirement:
    
    {text}
    
    Extract:
    - title
    - priority
    - risk level
    - summary
    """
)

structured_chain = structured_prompt | structured_llm


#-----------------------------------------------------
# Sequential Chain Example: Software Requirement Analysis
#-----------------------------------------------------

structured_llm = llm.with_structured_output(
    RequirementAnalysis
)

requirements_prompt = ChatPromptTemplate.from_template(
    """
    You are a senior software architect.

    Analyze the project requirement carefully.

    STRICT RULES:
    - Generate minimum 2 user stories
    - Generate minimum 3 implementation tasks
    - Task priorities must ONLY be:
      High, Medium, or Low
    - Keep project name concise
    - Risks should be technical risks only

    Requirement:
    {text}
    """
)

requirements_analyzer_chain = (
    requirements_prompt
    | structured_llm
)

#-------------------------------------------------------------------------------
# Parallel Chains
# ------------------------------------------------------------------------------

complexity_chain = (
    ChatPromptTemplate.from_template(
        """
        Analyze the technical complexity of this requirement:
        
        {text}
        
        Return ONLY:
        Complexity Level:
        Reason:
        """
    )
    | llm
    | parser
)

security_chain = (
    ChatPromptTemplate.from_template(
        """
        Analyze the security risks in this requirement:
        
        {text}
        
        Return:
        - Security Risks
        - Recommended Protections
        """
    )
    | llm
    | parser
)

scalability_chain = (
    ChatPromptTemplate.from_template(
        """
        Analyze the scalability concerns of this requirement:
        
        {text}
        
        Return:
        - Scalability Challenges
        - Suggested Improvements
        """
    )
    | llm
    | parser
)

parallel_analysis_chain = RunnableParallel(
    complexity=complexity_chain,
    security=security_chain,
    scalability=scalability_chain
)

#-------------------------------------------------------------------------------
# Router Chains
# ------------------------------------------------------------------------------

# Classifier chain
classifier_chain = (
    ChatPromptTemplate.from_template(
        """
        Classify this software requirement into ONE category:
        
        Categories:
        - security
        - scalability
        - authentication
        
        Requirement:
        {text}
        
        Choose the MOST dominant category.
        Return ONLY ONE word:
        - security
        - scalability
        - authentication
        """
    )
    | llm
    | parser
)

# Specialist chains

security_specialist_chain = (
    ChatPromptTemplate.from_template(
        """
        You are a cybersecurity architect.
        
        Analyze the security implications of:
        
        {text}
        """
    )
    | llm
    | parser
)

scalability_specialist_chain = (
    ChatPromptTemplate.from_template(
        """
        You are a distributed systems architect.
        
        Analyze the scalability concerns of:
        
        {text}
        """
    )
    | llm
    | parser
)

authentication_specialist_chain = (
    ChatPromptTemplate.from_template(
        """
        You are an authentication systems expert.
        
        Analyze the authentication design of:
        
        {text}
        """
    )
    | llm
    | parser
)

# Route mapping
routes = {
    "security": security_specialist_chain,
    "scalability": scalability_specialist_chain,
    "authentication": authentication_specialist_chain
}

# Router function
def route_requirement(inputs):
    
    category = classifier_chain.invoke(inputs).strip().lower()
    
    print(f"\n[ROUTER] Selected route: {category}\n")
    
    selected_chain = routes.get(
        category,
        security_specialist_chain
    )
    
    return selected_chain.invoke(inputs)

# Final router chain
router_chain = RunnableLambda(route_requirement)

#-------------------------------------------------------------------------------
# Conditional Chains
# ------------------------------------------------------------------------------

# Direct analysis chain
direct_analysis_chain = (
    ChatPromptTemplate.from_template(
        """
        Analyze this software requirement:
        
        {text}
        
        Return:
        - Main objective
        - Key risks
        - Suggested improvements
        """
    )
    | llm
    | parser
)

# Summarization chain
summary_chain = (
    ChatPromptTemplate.from_template(
        """
        Summarize this software requirement:
        
        {text}
        
        Keep only important technical details.
        """
    )
    | llm
    | parser
)

# Final analysis after summarization
summary_analysis_chain = (
    ChatPromptTemplate.from_template(
        """
        Analyze this summarized requirement:
        
        {text}
        
        Return:
        - Main objective
        - Key risks
        - Suggested improvements
        """
    )
    | llm
    | parser
)

# Conditional workflow function
def conditional_workflow(inputs):
    
    text = inputs["text"]
    
    # Deterministic Python logic
    if len(text) > 200:
        
        print("\n[CONDITIONAL] Long requirement detected → summarizing first\n")
        
        summarized = summary_chain.invoke({
            "text": text
        })
        
        return summary_analysis_chain.invoke({
            "text": summarized
        })
    
    else:
        
        print("\n[CONDITIONAL] Short requirement detected → direct analysis\n")
        
        return direct_analysis_chain.invoke(inputs)

# Final conditional chain
conditional_chain = RunnableLambda(conditional_workflow)