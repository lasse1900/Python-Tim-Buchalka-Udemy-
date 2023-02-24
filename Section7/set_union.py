'''
farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}

# all_animals = farm_animals | wild_animals
all_animals = farm_animals.union(wild_animals)
print(all_animals)
'''

from prescription_data import adverse_interactions

meds_to_watch = set()

'''
for interaction in adverse_interactions:
    # meds_to_watch = meds_to_watch.union(interaction)
    # meds_to_watch = meds_to_watch | interaction
    # meds_to_watch.update(interaction)
    meds_to_watch |= interaction   # update
'''

meds_to_watch.update(*adverse_interactions)

print(sorted(meds_to_watch))
print(*sorted(meds_to_watch), sep='\n')

