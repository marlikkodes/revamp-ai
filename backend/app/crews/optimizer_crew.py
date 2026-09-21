from crewai import Crew, Process

from app.agents.definitions import (
    create_conversion_agent,
    create_copy_agent,
    create_discovery_agent,
    create_performance_agent,
    create_report_agent,
    create_seo_agent,
    create_strategy_agent,
    create_ux_agent,
)
from app.tasks.definitions import (
    create_conversion_task,
    create_copy_task,
    create_discovery_task,
    create_performance_task,
    create_report_task,
    create_seo_task,
    create_strategy_task,
    create_ux_task,
)


def create_optimizer_crew() -> Crew:
    """Create the website optimization crew.

    Execution order (sequential):
        Discovery → SEO → UX → Copy → Performance → Conversion → Strategy → Report
    """
    # Create agents
    discovery_agent = create_discovery_agent()
    seo_agent = create_seo_agent()
    ux_agent = create_ux_agent()
    copy_agent = create_copy_agent()
    performance_agent = create_performance_agent()
    conversion_agent = create_conversion_agent()
    strategy_agent = create_strategy_agent()
    report_agent = create_report_agent()

    # Create tasks – order determines execution sequence
    discovery_task = create_discovery_task(discovery_agent)
    seo_task = create_seo_task(seo_agent)
    ux_task = create_ux_task(ux_agent)
    copy_task = create_copy_task(copy_agent)
    performance_task = create_performance_task(performance_agent)
    conversion_task = create_conversion_task(conversion_agent)
    strategy_task = create_strategy_task(strategy_agent)
    report_task = create_report_task(report_agent)

    crew = Crew(
        agents=[
            discovery_agent,
            seo_agent,
            ux_agent,
            copy_agent,
            performance_agent,
            conversion_agent,
            strategy_agent,
            report_agent,
        ],
        tasks=[
            discovery_task,
            seo_task,
            ux_task,
            copy_task,
            performance_task,
            conversion_task,
            strategy_task,
            report_task,
        ],
        process=Process.sequential,
        verbose=True,
    )

    return crew
