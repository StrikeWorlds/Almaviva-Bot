"""Utility functions for the Bad Version SIM application."""

import json
import random
from typing import Dict, List, Tuple

def load_json_data(file_path: str) -> dict:
    """Load and return JSON data from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Data file not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")

def load_countries() -> Dict[str, str]:
    """Load the countries and their flag emojis."""
    return load_json_data('data/countries.json')

def load_area_codes() -> List[int]:
    """Load the valid US area codes."""
    data = load_json_data('data/area_codes.json')
    return data['valid_codes']

def generate_phone_number(area_codes: List[int]) -> str:
    """Generate a random US phone number with a valid area code."""
    if not area_codes:
        raise ValueError("No valid area codes available")
    
    area_code = random.choice(area_codes)
    prefix = random.randint(200, 999)
    line = random.randint(1000, 9999)
    
    return f"+1-{area_code}-{prefix}-{line}"