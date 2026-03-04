"""
Configuration management for Fragmentation Bazaar.
Centralized config with environment variable validation.
"""
import os
from typing import Dict, Any, Optional
from pydantic import BaseSettings, Field, validator
from dataclasses import dataclass
import structlog

logger = structlog.get_logger(__name__)


class Settings(BaseSettings):
    """Application settings with environment