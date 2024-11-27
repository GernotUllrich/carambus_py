# services/game_service.py
import yaml
import logging
from django.utils.timezone import now
from carambus_py.models_xxx import Tournament

debug_logger = logging.getLogger("debug_logger")

def log_game_creation(game):
    debug_logger.debug(f"Game[NEW] - {game.gname} created at {now()}")

def deep_merge_data(game, new_data):
    """Merge new data into the game."""
    current_data = yaml.safe_load(game.data) or {}
    current_data.update(new_data)
    game.data = yaml.dump(current_data)
    game.save()

def deep_delete_data(game, key):
    """Delete a specific key from the game data."""
    current_data = yaml.safe_load(game.data) or {}
    removed_value = current_data.pop(key, None)
    game.data = yaml.dump(current_data)
    game.save()
    return removed_value
