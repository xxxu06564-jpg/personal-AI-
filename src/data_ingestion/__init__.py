"""
Data Ingestion Module - Handles data collection and preprocessing from multiple sources
"""

from .web_scraper import WebScraper
from .pdf_processor import PDFProcessor
from .json_loader import JSONLoader
from .data_processor import DataProcessor

__all__ = ["WebScraper", "PDFProcessor", "JSONLoader", "DataProcessor"]