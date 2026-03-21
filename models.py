from pydantic import BaseModel, Field
import json

class Trait(BaseModel):
    id: int
    name: str
    description: str

class Secret(BaseModel):
    id: int
    description: str
    revealedUnderPressure: bool
    
class Motive(BaseModel):
    id: int
    name: str
    weight: float = Field(gt=0.0, le=1.0)
    traits_affinity: list[int] | list[Trait] = []
    
class Weapon(BaseModel):
    id: int
    name: str
    weight: float = Field(gt=0.0, le=1.0)
    description: str
    
class Suspect(BaseModel):
    id: int
    name: str
    traits: list[Trait] | list[int] = []
    secrets: list[Secret] | list[int] = []
    motive: Motive | None = None
    
class Solution(BaseModel):
    culpritID: int
    victimID: int
    motive: Motive
    weapon: Weapon
    
class GeneratorConfig(BaseModel):
    suspect_count: int
    motive_pool: list[Motive]
    weapon_pool: list[Weapon]
    trait_pool: list[Trait]
    secret_pool: list[Secret]
    seed: int | None = None
    
    
class Case(BaseModel): # OUTPUT CLASS
    suspects: list[Suspect]
    solution: Solution
    
def load_config(filepath: str) -> GeneratorConfig:
    with open(filepath, 'r') as config_file:
        config = GeneratorConfig.model_validate(json.load(config_file))
        
    return config

