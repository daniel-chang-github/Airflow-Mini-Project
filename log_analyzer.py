from pathlib import Path
from pprint import pprint

path = 'mnt/airflow/logs/marketvol2'

def analyze_file(**kwargs):
    logfiles = Path(path).rglob('*.log')
    error_count = 0
    error_lines = []
    for file in logfiles:
        # print(file)
        with open(file, 'r') as logfile:
            for line in logfile:
                if 'ERROR' in line:
                    error_count += 1
                    error_lines.append(str(file) + '\n' + line  )
    pprint(error_count) 
    pprint(error_lines)


analyze_file()
