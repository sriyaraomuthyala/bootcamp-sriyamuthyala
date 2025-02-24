from abc import ABC, abstractmethod

class PersistentQInterface(ABC):
    @abstractmethod
    def enqueue(self, job_id: str, job_data: str):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def mark_done(self, job_id: str):
        pass
