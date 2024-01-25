from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        salaries_list = list(
            int(job['max_salary'])
            for job in self.jobs_list
            if job['max_salary'].isdigit()
        )
        return max(salaries_list)

    def get_min_salary(self) -> int:
        salaries_list = list(
            int(job['min_salary'])
            for job in self.jobs_list
            if job['min_salary'].isdigit()
        )
        return min(salaries_list)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
