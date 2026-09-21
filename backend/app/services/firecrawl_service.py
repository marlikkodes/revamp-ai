import logging
import os

from firecrawl import FirecrawlApp

logger = logging.getLogger(__name__)


class FirecrawlService:
    """Service for scraping websites using Firecrawl."""

    def __init__(self):
        api_key = os.getenv("FIRECRAWL_API_KEY")
        if not api_key:
            raise ValueError("FIRECRAWL_API_KEY environment variable is not set")
        self.app = FirecrawlApp(api_key=api_key)
        self.params = {
            "formats": ["markdown"]
        }

    def scrape(self, url: str) -> str:
        """Scrape a website and return its content as markdown."""
        logger.info(f"Scraping URL: {url}")

        result = self.app.scrape_url(url, **self.params)

        # Handle dict response
        if isinstance(result, dict):
            content = result.get("markdown") or result.get("content") or str(result)
            logger.info(f"Scraped {len(content)} characters")
            return content

        # Handle object response (newer firecrawl-py versions)
        if hasattr(result, "markdown") and result.markdown:
            logger.info(f"Scraped {len(result.markdown)} characters")
            return result.markdown

        raw = str(result)
        logger.info(f"Scraped {len(raw)} characters (raw)")
        return raw
