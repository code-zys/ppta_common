from typing import Any, Dict, Optional


class CollectEmailsDto():
    override: Optional[bool] = False
    run_process: Dict[str, Any]

    def __init__(self, override=None, run_process=None):
        self.override = override
        self.run_process = run_process

    def to_dict(self) -> Dict[str, Any]:
        return { 'override': self.override, 'run_process': self.run_process }