
"""
Utility functions for printing configurations and other information in a nice format.
"""

def print_configuration(configuration: dict, title: str | None = None, sort_keys: bool = False):
    """
    Print a single-level configuration dictionary in a nice format. 
    Optionally, include a title.
    """
    if title is not None:
        print(f"{title}")
    # Sort the configuration by keys if requested
    if sort_keys:
        configuration = dict(sorted(configuration.items()))
    
    # Determine the maximum key and value lengths for alignment
    max_key_len = max(len(str(k)) for k in configuration)
    max_val_len = max(len(str(v)) for v in configuration.values())
    # Print each key-value pair with aligned formatting
    for key, value in configuration.items():
        print(f" - {key:<{max_key_len}} : {str(value):>{max_val_len}}")