from prescription_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny", "John"]

# Remove Warfarin and add Edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except KeyError:
        print(f"\nPatient {patient} is not taking warfarin"
              f"Please remove {patient} from the trial run")
    print(patient, prescription)