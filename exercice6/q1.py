import re
from pathlib import Path
from typing import List


"""
Fake logs, generated on https://www.logs.to/
Regex tool : https://regex101.com/
"""

BASE_DIR = Path(__file__).resolve().parent.parent


class RegexLog:
    PATH_TO_LOG_FILE = f"{BASE_DIR}/statics/20220803234120.cef"

    def __init__(self, regex: re.Pattern) -> List:
        regex = re.compile(self._regex_str)
        self.logs = regex.findall(
            self.read_log_file()
        )

    @classmethod
    def read_log_file(cls) -> str:
        return open(cls.PATH_TO_LOG_FILE, "r").read()

    def __str__(self):
        return "RegexLog"


class InfoRadiusLog(RegexLog):
    _regex_str = ".*CISE_RADIUS_Diagnostics\|(.*)INFO(.*)"

    def __init__(self):
        super().__init__(self._regex_str)

    def __str__(self):
        return "InfoRadiusLog"


class WarnRadiusLog(RegexLog):
    _regex_str = ".*CISE_RADIUS_Diagnostics\|(.*)WARN(.*)"

    def __init__(self):
        super().__init__(self._regex_str)

    def __str__(self):
        return "WarnRadiusLog"


class WarnAuditLog(RegexLog):
    _regex_str = ".*CISE_Administrative_and_Operational_Audit\|(.*)WARN(.*)"

    def __init__(self):
        super().__init__(self._regex_str)

    def __str__(self):
        return "WarnAuditLog"
