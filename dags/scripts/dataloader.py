import uuid
import pandas as pd

class DataLoader:
    """A class for loading the data
    """
    def read_csv(self, filename):
        """
        Read csv file and return the header and rows
        Args:
            filename: The path of the file
        Return:
            (header, rows): list of headers and rows
        """
        headers = []
        rows = []
        with open(filename, 'r') as file:
            lines = file.readlines()
            headers.extend(lines[0].strip('\n').split(';'))
            rows.extend(list(map(lambda line: line.strip('\n'), lines[1:])))
        return headers, rows
    
    def data_to_dataframe(self, headers, rows):
        """
        Extract the data from csv and put into dataframe
        Args:
            headers: headers of the data
            rows: The rows
        Return:
            Tuple of vehicle and trajectories dataframe
        """
        vehicle_data = {
            "uid": [],
            headers[0]: [],
            headers[1]: [],
            headers[2]: [],
            headers[3]: []
        }
        trajectories_data = {
            "uid": [],
            headers[4]: [],
            headers[5]: [],
            headers[6]: [],
            headers[7]: [],
            headers[8]: [],
            headers[9]: []
            }
        
        for idx, row in enumerate(rows):
            uid = uuid.uuid4().hex
            line = row.split('; ')[:-1]
            vehicle_data["uid"].append(uid)
            vehicle_data[headers[0]].append(int(line[0]))
            vehicle_data[headers[1]].append(line[1])
            vehicle_data[headers[2]].append(float(line[2]))
            vehicle_data[headers[3]].append(float(line[3]))
            for i in range(0, (len(line) // 6)*6, 6):
                trajectories_data["uid"].append(uid)
                trajectories_data[headers[4]].append(float(line[4+i]))
                trajectories_data[headers[5]].append(float(line[4+i+1]))
                trajectories_data[headers[6]].append(float(line[4+i+2]))
                trajectories_data[headers[7]].append(float(line[4+i+3]))
                trajectories_data[headers[8]].append(float(line[4+i+4]))
                trajectories_data[headers[9]].append(float(line[4+i+5]))

        vehicle_data_df = pd.DataFrame(vehicle_data).reset_index(drop=True)
        trajectories_data_df = pd.DataFrame(trajectories_data).reset_index(drop=True)

        return vehicle_data_df, trajectories_data_df