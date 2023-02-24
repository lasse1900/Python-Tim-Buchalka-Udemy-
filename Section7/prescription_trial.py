from prescription_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# Remove Warfarin and add Edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    if warfarin in prescription:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    else:
        print(f"\nPatient {patient} is not taking warfarin"
              f"Please remove {patient} from the trial run\n")
    print(patient, prescription)