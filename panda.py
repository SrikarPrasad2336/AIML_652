import pandas as pd

patient_data = {
    'Patient Name': ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown'],
    'Age': [5, 3, 7, 2],
    'Date of Appointment': ['2025-01-22', '2025-01-23', '2025-01-24', '2025-01-25'],
    'Patient ID': [101, 102, 103, 104]
}

patient_df = pd.DataFrame(patient_data)

drag_quantity_data = {
    'Drag Name': ['Drag A', 'Drag B', 'Drag C', 'Drag D'],
    'Quantity': [1, 3, 2, 4],
    'Patient ID': [101, 102, 103, 104]
}

drag_quantity_df = pd.DataFrame(drag_quantity_data)

filtered_patient_df = patient_df[patient_df['Age'] < 6][['Patient Name', 'Age']]

print(filtered_patient_df)
