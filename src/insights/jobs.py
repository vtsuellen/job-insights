from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path) as file:
            reader = csv.DictReader(file)
            self.jobs_list = list(reader)

    def get_unique_job_types(self) -> List[str]:
        job_types = set()

        for job in self.jobs_list:
            job_types.add(job["job_type"])

        return list(job_types)

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
