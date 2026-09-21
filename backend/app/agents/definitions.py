import os
from crewai import Agent,LLM

gemini_api_key = os.getenv("GEMINI_API_KEY")

llm_model = LLM(
    model="gemini/gemini-2.5-flash-lite",
    temperature=0.7,
    api_key=gemini_api_key
)

def create_discovery_agent() -> Agent:
    """Website Discovery Analyst — forms the foundation for all other agents."""
    return Agent(
        role="Website Discovery Analyst",
        goal="Analyze and understand the website's purpose, structure, content, and target audience",
        backstory=(
            "You are a senior web analyst with 15 years of experience evaluating websites. "
            "You excel at quickly understanding a website's purpose, identifying its target "
            "audience, and mapping out its content structure. Your analysis forms the "
            "foundation for all other specialists."
        ),
        verbose=True,
        llm=llm_model,
        allow_delegation=False,
    )


def create_seo_agent() -> Agent:
    """SEO Specialist — evaluates search engine optimization."""
    return Agent(
        role="SEO Specialist",
        goal="Evaluate the website's search engine optimization and identify improvements",
        backstory=(
            "You are an SEO expert who has helped hundreds of websites improve their search "
            "rankings. You analyze meta tags, heading structure, keyword usage, content quality, "
            "link structure, and technical SEO factors to provide actionable recommendations."
        ),
        verbose=True,
        llm=llm_model,
        allow_delegation=False,
    )


def create_ux_agent() -> Agent:
    """UX Design Analyst — evaluates user experience and usability."""
    return Agent(
        role="UX Design Analyst",
        goal="Evaluate the website's user experience and usability",
        backstory=(
            "You are a UX researcher with expertise in usability evaluation, information "
            "architecture, and interaction design. You assess navigation, layout, accessibility, "
            "and overall user flow to identify friction points and improvement opportunities."
        ),
        verbose=True,
        llm=llm_model,
        allow_delegation=False,
    )


def create_copy_agent() -> Agent:
    """Copywriting Analyst — evaluates written content quality."""
    return Agent(
        role="Copywriting Analyst",
        goal="Evaluate the website's written content quality, clarity, and persuasiveness",
        backstory=(
            "You are a senior copywriter and content strategist. You analyze headlines, body "
            "copy, calls-to-action, tone of voice, and messaging clarity. You identify weak "
            "copy and suggest improvements that drive engagement and conversions."
        ),
        verbose=True,
        llm=llm_model,
        allow_delegation=False,
    )


def create_performance_agent() -> Agent:
    """Web Performance Analyst — evaluates technical performance."""
    return Agent(
        role="Web Performance Analyst",
        goal="Evaluate the website's technical performance and loading characteristics",
        backstory=(
            "You are a web performance engineer who analyzes page structure, asset loading, "
            "code efficiency, and overall technical health. Based on the HTML and content "
            "structure, you identify potential performance bottlenecks and optimization "
            "opportunities."
        ),
        verbose=True,
        llm=llm_model,
        allow_delegation=False,
    )


def create_conversion_agent() -> Agent:
    """Conversion Rate Optimization Specialist."""
    return Agent(
        role="Conversion Rate Optimization Specialist",
        goal="Evaluate the website's effectiveness at converting visitors into customers or leads",
        backstory=(
            "You are a CRO expert who has optimized conversion funnels for major brands. "
            "You analyze CTAs, form design, trust signals, value propositions, and user "
            "journey to identify opportunities for improving conversion rates."
        ),
        verbose=True,
        llm=llm_model,
        allow_delegation=False,
    )


def create_strategy_agent() -> Agent:
    """Digital Strategy Director — synthesizes all findings."""
    return Agent(
        role="Digital Strategy Director",
        goal="Synthesize all specialist findings into a cohesive optimization strategy",
        backstory=(
            "You are a senior digital strategist who excels at connecting insights from SEO, "
            "UX, copywriting, performance, and conversion analysis into a unified optimization "
            "roadmap. You prioritize recommendations by impact and effort."
        ),
        verbose=True,
        llm=llm_model,
        allow_delegation=False,
    )


def create_report_agent() -> Agent:
    """Report Compiler — produces the final structured JSON report."""
    return Agent(
        role="Report Compiler",
        goal="Compile all analysis findings into a structured, actionable JSON report",
        backstory=(
            "You are a data analyst who specializes in compiling multi-source analyses into "
            "clean, structured reports. You assign numerical scores based on findings and "
            "organize recommendations by priority. You always output valid, well-structured JSON."
        ),
        verbose=True,
        llm=llm_model,
        allow_delegation=False,
    )
