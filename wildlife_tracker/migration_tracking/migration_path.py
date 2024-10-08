from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat


class MigrationPath:

    def __init__(self, destination: Habitat,
                 species: str,
                 start_location: Habitat,
                 duration: Optional[int] = None):
        self.destination = destination
        self.duration = duration
        self.start_location = start_location
        self.species = species
        
    # create constructor
    pass