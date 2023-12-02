# REP (Reuse/Release equivalence principle -> make a component of those classes that share the same purpose)
# CCP (common closure principle ~ single responsibility)
# CRP (common reuse principle ~ interface segregation)

# REP && CCP && CRP violation:
# module 1 (String formatting library) ->
class StrConverter: ...
class ConvertStrToInt: ...
class CalculateComplexNumber: ...
# This module violates all of those principles
# because classes in it don't share the same purpose, change
# at different times and for different reasons, and 
# forse users of this library to depend on something they 
# don't need. It seems like those 3 principles and their violations
# are very tightly coupled.

# fix:
# module 1 (String formatting library) ->
class StrConverter: ...
class ConvertStrToInt: ...
# module 2 (Complex number processing library) ->
class CalculateComplexNumber: ...


# ------------ addit ------------
# OCP
# violation for a component:
# module 1
import LowLvlCode
class HighLvlCode:
    def call_low_lvl_code(self):
        LowLvlCode().do_some()

# module 2
class LowLvlCode:
    def do_some(self): ...

# fix:
# module 1
class LowLvlCodeInterface(ABC):
    @abstractmethod
    def do_some(self): ...

class HighLvlCode:
    low_lvl_code_obj: LowLvlCodeInterface

    def __init__(self, low_lvl_code: LowLvlCodeInterface) -> None:
        self.low_lvl_code_obj = low_lvl_code

    def call_low_lvl_code(self):
        self.low_lvl_code_obj.do_some()

# module 2
import LowLvlCodeInterface
import HighLvlCode

class LowLvlCode(LowLvlCodeInterface):
    def do_some(self): ...

def main():
    res = HighLvlCode(LowLvlCode()).call_low_lvl_code()

