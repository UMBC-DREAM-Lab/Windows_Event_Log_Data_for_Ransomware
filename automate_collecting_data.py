import os
import pandas as pd

# Define paths based on your structure
base_dir = "<path_to_file>"
server_folder = os.path.join(base_dir, "server_vm")
victim_folder = os.path.join(base_dir, "victim_vm")
output_base_dir = "<path_to_output_file>"

# Function to process and save updated CSVs
def update_and_save_csv(root_folder, machine_type):
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)

        # Ensure it's a valid ransomware hash folder (ran_{hash})
        if os.path.isdir(folder_path) and folder_name.startswith("ran_"):
            hash_val = folder_name.replace("ran_", "")  # Extract hash value
            
            # Create output folder in hash_data_combined
            output_folder = os.path.join(output_base_dir, machine_type, folder_name)
            os.makedirs(output_folder, exist_ok=True)

            for file in os.listdir(folder_path):
                if file.endswith(".csv"):
                    file_path = os.path.join(folder_path, file)
                    
                    # Read CSV
                    df = pd.read_csv(file_path)
                    
                    # Add metadata columns
                    df['Hash'] = hash_val
                    df['Machine'] = machine_type
                    
                    # Save modified CSV in the new directory
                    output_file_path = os.path.join(output_folder, file)
                    df.to_csv(output_file_path, index=False)
                    print(f"Processed and saved: {output_file_path}")

# Run the function for both server and victim logs
update_and_save_csv(server_folder, "Server_new")
update_and_save_csv(victim_folder, "Victim_new")

print("Step 1 completed: Updated CSV files saved in /data/hash_data_combined!")

--------STEP 2----------------

 # Define the processed data directory
 combined_data_dir = "<path_to_output_file>"
 output_file = os.path.join(combined_data_dir, "merged_logs.csv")

 # Function to merge all CSV files into one DataFrame
 def merge_all_logs(root_folder):
     all_data = pd.DataFrame()  # Empty DataFrame to store merged data

     for machine_type in ["Server", "Victim"]:  # Loop through both folders
         machine_folder = os.path.join(root_folder, machine_type)
        
         for folder_name in os.listdir(machine_folder):  # Iterate through hash folders
             folder_path = os.path.join(machine_folder, folder_name)
            
             if os.path.isdir(folder_path):  # Ensure it's a folder
                 for file in os.listdir(folder_path):
                     if file.endswith(".csv"):
                         file_path = os.path.join(folder_path, file)
                        
                         # Read CSV
                         df = pd.read_csv(file_path)
                        
                         # Append to main DataFrame
                         all_data = pd.concat([all_data, df], ignore_index=True)

     return all_data

 # Merge logs
 merged_logs = merge_all_logs(combined_data_dir)

 # Save the final merged dataset
 merged_logs.to_csv(output_file, index=False)

 print(f"Step 2 completed: Merged dataset saved as {output_file}!")

--------STEP 3----------------

 # List of hash values to iterate over - 20 total samples
 hashes = ["10aa058a3ac49e016cad7987b8e09886",
 "1dd464cbb3fbd6881eef3f05b8b1fbd5",
 "3317daace715dc332622d883091cf68b",
 "38035325b785329e3f618b2a0b90eb75",
 "50c4970003a84cab1bf2634631fe39d7",
 "6c209fa3f2714871eb08941ec305a65f",
 "9ef073ca0e0133727252b999f346c269",
 "6bbc3c265fe20dcad4131afbbc06a287",
 "1c7744d75dc99bb8bc8c8724376d4997",
 "6c209fa3f2714871eb08941ec305a65f",
 "0c4502d6655264a9aa420274a0ddeaeb",
 "0d37accb48619ea4db6ebde09481f768",
 "0c63503795ddda951bf11a589679a6ee",
 "1c3bcfb20d1f44f3eb4281e587d263bb",
 "0b12d73024ea2b1755d6a6cc9dd551cd",
 "0b91ce46f89f342be4ebc72ba5a1f6b5",
 "0c89c5856a8d38dba2cf2c42aface0c5",
 "0cc1e87eb07f9452a3036b2113b8d010",
 "10b3fd3c861d5cf657934c89260590ab",
 "15f9bc49b11aa4498509a20dfdb2c22e"]


 #start the loop

 for hash_val in hashes:

     #Read the application logs collected 
     app_log_path = <new_output_file>

     ran3 = pd.read_csv(
         app_log_path,
         sep=',',            # Adjust delimiter
         header=None,        # No header
         names=['Level', 'Date and Time', 'Source', 'Event ID', 'Task Category', 'Message'],  # Define column names
         skiprows=[0],

     )

     # Convert "Date and Time" column to datetime format
     ran3['Date and Time'] = pd.to_datetime(ran3['Date and Time'])

     # Filter rows by a specific date
     ran3 = ran3[ran3['Date and Time'].dt.date == pd.Timestamp('2/5/2024').date()]

     #Add a column to represent a unique identification number
     ran3["uniq_id"] = hash_val

     sec_log_path = <path_file>

     ran3_s = pd.read_csv(sec_log_path,
                         sep=',',            # Adjust delimiter
         header=None,        # No header
         names=['Keywords', 'Date and Time', 'Source', 'Event ID', 'Task Category', 'Message'],  # Define column names
         skiprows=[0],
         )

     # Convert "Date and Time" column to datetime format
     ran3_s['Date and Time'] = pd.to_datetime(ran3_s['Date and Time'])

     # Filter rows by a specific date
     ran3_s= ran3_s[ran3_s['Date and Time'].dt.date == pd.Timestamp('2/5/2024').date()]


     #Add a column to represent a unique identification number
     ran3_s["uniq_id"] = hash_val


     sys_log_path = <path_file>

     ran3_ss = pd.read_csv(sys_log_path, 
                         sep=',',            # Adjust delimiter
         header=None,        # No header
         names=['Level', 'Date and Time', 'Source', 'Event ID', 'Task Category', 'Message'],  # Define column names
         skiprows=[0],  # Replace with the row number of the repeated header
         )

     # Convert "Date and Time" column to datetime format
     ran3_ss['Date and Time'] = pd.to_datetime(ran3_ss['Date and Time'])

     # Filter rows by a specific date
     ran3_ss = ran3_ss[ran3_ss['Date and Time'].dt.date == pd.Timestamp('2/5/2024').date()]

     #Add a column to represent a unique identification number
     ran3_ss["uniq_id"] = hash_val


     #merge the dataframes and store the results
     import os
     # merged_df = pd.merge(ran3, ran3_s, on='uniq_id')
     # merged_df = pd.merge(merged_df, ran3_ss, on='uniq_id')
     merged_df = pd.concat([ran3, ran3_s, ran3_ss], ignore_index=True)
     print(merged_df)
     print("Databse concatenated for server data {hash_val}")
     output_dir = <path_file>
     output_file = f"ran_{hash_val}.csv"
     output_path = os.path.join(output_dir, output_file)
     merged_df.to_csv(output_path, index=False)
     print(f"Merged data saved to: {output_path}")


--------STEP 4----------------


     #Read the logs collected - victim

     app_log_path_v = <path_file>

     ran4 = pd.read_csv(
         app_log_path_v,
         sep=',',            # Adjust delimiter
         header=None,        # No header
         names=['Level', 'Date and Time', 'Source', 'Event ID', 'Task Category', 'Message'],  # Define column names
         skiprows=[0],

     )

     # Convert "Date and Time" column to datetime format
     ran4['Date and Time'] = pd.to_datetime(ran4['Date and Time'])

     # Filter rows by a specific date
     ran4 = ran4[ran4['Date and Time'].dt.date == pd.Timestamp('2/5/2024').date()]

     #Add a column to represent a unique identification number
     ran4["uniq_id"] = hash_val

     sec_log_path_v = <path_file>

     ran4_s = pd.read_csv(sec_log_path_v,
                         sep=',',            # Adjust delimiter
         header=None,        # No header
         names=['Keywords', 'Date and Time', 'Source', 'Event ID', 'Task Category', 'Message'],  # Define column names
         skiprows=[0],  # Replace with the row number of the repeated header
         )

     # Convert "Date and Time" column to datetime format
     ran4_s['Date and Time'] = pd.to_datetime(ran4_s['Date and Time'])

     # Filter rows by a specific date
     ran4_s= ran4_s[ran4_s['Date and Time'].dt.date == pd.Timestamp('12/4/2024').date()]


     #Add a column to represent a unique identification number
     ran4_s["uniq_id"] = hash_val


     sys_log_path_v = <path_file>

     ran4_ss = pd.read_csv(sys_log_path_v, 
                         sep=',',            # Adjust delimiter
         header=None,        # No header
         names=['Level', 'Date and Time', 'Source', 'Event ID', 'Task Category', 'Message'],  # Define column names
         skiprows=[0],  # Replace with the row number of the repeated header
         )

     # Convert "Date and Time" column to datetime format
     ran4_ss['Date and Time'] = pd.to_datetime(ran4_ss['Date and Time'])

     # Filter rows by a specific date
     ran4_ss = ran4_ss[ran4_ss['Date and Time'].dt.date == pd.Timestamp('12/4/2024').date()]

     #Add a column to represent a unique identification number
     ran4_ss["uniq_id"] = hash_val


     # merged_df = pd.merge(ran4, ran4_s, on='uniq_id')
     # merged_df = pd.merge(merged_df, ran4_ss, on='uniq_id')
     merged_df1 = pd.concat([ran4, ran4_s, ran4_ss], ignore_index=True)
     print(merged_df1)
     print("Databse concatenated for victim data")
     output_dir = <path_file>
     output_file = f"ran_{hash_val}.csv"
     output_path = os.path.join(output_dir, output_file)
     merged_df1.to_csv(output_path, index=False)



