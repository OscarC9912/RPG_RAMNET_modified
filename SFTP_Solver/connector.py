from SFTP_Solver.copier import SFTP_copier
from SFTP_Solver.dataLoader import dataLoader


# class connector:

#     def __init__(self) -> None:

#         copier = SFTP_copier()
#         load = dataLoader(copier)
#         self.loader = load

copier = SFTP_copier()
loader = dataLoader(copier)