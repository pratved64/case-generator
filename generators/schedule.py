from models import *
from random import Random
from datetime import timedelta, datetime

def pick_crime_slot(config: GeneratorConfig, rng: Random):
    selected_slot = rng.randint(1,config.slot_count-2)
    return selected_slot

def subset_rooms(config: GeneratorConfig, num_rooms: int, rng: Random) -> list[Room]:
    rs: list[Room] = rng.sample(config.room_pool, num_rooms)
    if not any(room.positionState == PositionState.CRIME_ROOM for room in rs): # wtf is this
        rndIdx = rng.randint(0, len(rs) - 1)
        rs[rndIdx] = rs[rndIdx].model_copy(update={"positionState": PositionState.CRIME_ROOM})    
    
    return rs

def generate_schedule(suspect: Suspect, rooms: list[Room], config: GeneratorConfig, rng: Random):
    slots = []
    current_time = datetime.combine(datetime.today(), config.start_slot)
    for i in range(config.slot_count):
        current_time = current_time + timedelta(minutes=30)
        selected_room = rng.sample(rooms, 1)[0]
        slot = ScheduleSlot(slotID=i, timeLabel=current_time.strftime("%H:%M"), roomID=selected_room.id)
        slots.append(slot)
        
    return Schedule(slots=slots)