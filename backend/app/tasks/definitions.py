from crewai import Agent, Task


def create_discovery_task(agent: Agent) -> Task:
    """Task for the Discovery Agent to analyze the website."""
    return Task(
        description=(
            "Analyze the following website and provide a comprehensive overview.\n\n"
            "URL: {url}\n\n"
            "Website Content:\n{website_content}\n\n"
            "Provide:\n"
            "1. Website's primary purpose and business type\n"
            "2. Target audience\n"
            "3. Key content areas and pages\n"
            "4. Brand messaging and tone\n"
            "5. Products or services offered\n"
            "6. Overall first impression"
        ),
        expected_output=(
            "A detailed overview covering the website's purpose, audience, content "
            "structure, brand voice, and key observations that will inform specialist analyses."
        ),
        agent=agent,
    )


def create_seo_task(agent: Agent) -> Task:
    """Task for the SEO Agent."""
    return Task(
        description=(
            "Based on the discovery analysis and the website content, evaluate the SEO.\n\n"
            "Analyze:\n"
            "1. Title tags and meta descriptions\n"
            "2. Heading hierarchy (H1, H2, H3 usage)\n"
            "3. Keyword usage and density\n"
            "4. Content quality and relevance\n"
            "5. Internal/external link structure\n"
            "6. Image alt text and optimization\n"
            "7. URL structure\n\n"
            "Provide a score from 0-100 and specific recommendations."
        ),
        expected_output=(
            "SEO analysis with a score (0-100), key findings, and 3-5 specific, actionable "
            "recommendations. Format: 'SEO Score: X/100' followed by findings and recommendations."
        ),
        agent=agent,
    )


def create_ux_task(agent: Agent) -> Task:
    """Task for the UX Agent."""
    return Task(
        description=(
            "Based on the discovery analysis and the website content, evaluate the user experience.\n\n"
            "Analyze:\n"
            "1. Navigation clarity and structure\n"
            "2. Content layout and readability\n"
            "3. Mobile responsiveness indicators\n"
            "4. Visual hierarchy\n"
            "5. Accessibility considerations\n"
            "6. User flow and information architecture\n\n"
            "Provide a score from 0-100 and specific recommendations."
        ),
        expected_output=(
            "UX analysis with a score (0-100), key findings, and 3-5 specific recommendations. "
            "Format: 'UX Score: X/100' followed by findings and recommendations."
        ),
        agent=agent,
    )


def create_copy_task(agent: Agent) -> Task:
    """Task for the Copy Agent."""
    return Task(
        description=(
            "Based on the discovery analysis and the website content, evaluate the copywriting.\n\n"
            "Analyze:\n"
            "1. Headline effectiveness\n"
            "2. Value proposition clarity\n"
            "3. Call-to-action strength\n"
            "4. Tone consistency\n"
            "5. Grammar and readability\n"
            "6. Persuasion techniques\n\n"
            "Provide a score from 0-100 and specific recommendations."
        ),
        expected_output=(
            "Copy analysis with a score (0-100), key findings, and 3-5 specific recommendations. "
            "Format: 'Copy Score: X/100' followed by findings and recommendations."
        ),
        agent=agent,
    )


def create_performance_task(agent: Agent) -> Task:
    """Task for the Performance Agent."""
    return Task(
        description=(
            "Based on the discovery analysis and the website content, evaluate technical performance.\n\n"
            "Analyze:\n"
            "1. Page structure complexity\n"
            "2. Resource loading patterns (scripts, styles, images)\n"
            "3. Code efficiency indicators\n"
            "4. Third-party dependencies\n"
            "5. Caching and optimization opportunities\n"
            "6. Overall technical health\n\n"
            "Provide a score from 0-100 and specific recommendations."
        ),
        expected_output=(
            "Performance analysis with a score (0-100), key findings, and 3-5 specific "
            "recommendations. Format: 'Performance Score: X/100' followed by findings and recommendations."
        ),
        agent=agent,
    )


def create_conversion_task(agent: Agent) -> Task:
    """Task for the Conversion Agent."""
    return Task(
        description=(
            "Based on the discovery analysis and the website content, evaluate conversion optimization.\n\n"
            "Analyze:\n"
            "1. Call-to-action placement and design\n"
            "2. Trust signals (testimonials, badges, social proof)\n"
            "3. Form design and friction\n"
            "4. Value proposition visibility\n"
            "5. Urgency and scarcity elements\n"
            "6. Conversion funnel clarity\n\n"
            "Provide a score from 0-100 and specific recommendations."
        ),
        expected_output=(
            "Conversion analysis with a score (0-100), key findings, and 3-5 specific "
            "recommendations. Format: 'Conversion Score: X/100' followed by findings and recommendations."
        ),
        agent=agent,
    )


def create_strategy_task(agent: Agent) -> Task:
    """Task for the Strategy Agent to synthesize all findings."""
    return Task(
        description=(
            "Review all the specialist analyses (SEO, UX, Copy, Performance, Conversion) "
            "and synthesize them into a unified optimization strategy.\n\n"
            "Provide:\n"
            "1. Executive summary of the website's overall health\n"
            "2. Top 3 most critical issues across all areas\n"
            "3. Quick wins that can be implemented immediately\n"
            "4. Long-term strategic recommendations\n"
            "5. Priority ranking of all recommendations by impact and effort"
        ),
        expected_output=(
            "A strategic synthesis with prioritized recommendations, quick wins, "
            "and a clear roadmap for optimization across all analyzed areas."
        ),
        agent=agent,
    )


def create_report_task(agent: Agent) -> Task:
    """Task for the Report Agent to compile the final structured JSON report."""
    return Task(
        description=(
            "Compile all specialist analyses and the strategy synthesis into a final structured report.\n\n"
            "You MUST output a valid JSON object with EXACTLY this structure:\n"
            "{{\n"
            '  "overall_score": <integer 0-100, weighted average of all scores>,\n'
            '  "seo_score": <integer 0-100, from SEO analysis>,\n'
            '  "ux_score": <integer 0-100, from UX analysis>,\n'
            '  "copy_score": <integer 0-100, from Copy analysis>,\n'
            '  "performance_score": <integer 0-100, from Performance analysis>,\n'
            '  "conversion_score": <integer 0-100, from Conversion analysis>,\n'
            '  "summary": "<2-3 paragraph executive summary>",\n'
            '  "recommendations": [\n'
            "    {{\n"
            '      "category": "<seo|ux|copy|performance|conversion>",\n'
            '      "priority": "<high|medium|low>",\n'
            '      "title": "<short recommendation title>",\n'
            '      "description": "<detailed actionable description>"\n'
            "    }}\n"
            "  ]\n"
            "}}\n\n"
            "Extract the scores from each specialist's analysis. "
            "Calculate overall_score as the average of all five scores. "
            "Include the top 8-12 most impactful recommendations across all categories.\n\n"
            "CRITICAL: Output ONLY the JSON object. No additional text before or after."
        ),
        expected_output=(
            "A valid JSON object matching the specified schema with scores, summary, "
            "and recommendations."
        ),
        agent=agent,
    )
