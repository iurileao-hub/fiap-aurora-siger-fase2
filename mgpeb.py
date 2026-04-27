
from collections import deque
from dataclasses import dataclass
from typing import Optional, List, Tuple, Any
from enum import Enum
import time
import random

# =============================================================================
# [1] Data - Classes struct
# =============================================================================

class ModuleType(Enum):
    HABITAT = "habitation"
    ENERGY = "energy"
    LAB = "laboratory"
    LOGISTIC = "Logistic"
    MEDICAL = "Medical support"
    
class AtmosfericClassifier(Enum):
    GREEN = "OK"
    YELLOW = "CAUTION"
    RED = "DANGER"
    
class StopCondition(Enum):
    WAITING = "Waiting autorization"
    AUTORIZED = "Autorized stop"
    DENIED = "Denied stop"
    EMERGENCY = "Emergency post"
    STOPPED = "Stopped"
    
@dataclass
class Module: 
    """
    Represents a module to Mars
    """
    
    id: int
    type: ModuleType
    weight: float
    arrival_time: float
    stop_condition: StopCondition = StopCondition.WAITING
    
    def __str__(self):
        return f"Module {self.id} - Type: {self.type.value}, Weight: {self.weight}kg, Arrival: {time.ctime(self.arrival_time)}, Condition: {self.stop_condition.value}"
    
    def __lt__(self, other):
        """Defines the less-than operator for sorting modules by arrival time."""
        return self.arrival_time < other.arrival_time
    
# === Algorithms for searching and sorting === 

class SearchAlgorithms:
    
    @staticmethod
    def linear_search():
        pass
    
    @staticmethod
    def binary_search():
        pass
    
    
# =============================================================================
# [2] ESTRUTURAS LINEARES — Operações de fila, pilha e verificação
# =============================================================================


# =============================================================================
# [3] REGRAS LÓGICAS — Autorização de pouso com expressões booleanas
# =============================================================================


# =============================================================================
# [4] BUSCA — Algoritmos de busca linear
# =============================================================================


# =============================================================================
# [5] ORDENAÇÃO — Bubble Sort e Selection Sort
# =============================================================================


# =============================================================================
# [6] FUNÇÕES MATEMÁTICAS — Modelagem de fenômenos do pouso
# =============================================================================


# =============================================================================
# [7] SIMULAÇÃO — Execução do pouso sequencial
# =============================================================================


# =============================================================================
# [8] EXIBIÇÃO E MENU — Interface com o operador
# =============================================================================


# =============================================================================
# Ponto de entrada
# =============================================================================