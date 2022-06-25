from SFTP_Solver.copier import SFTP_copier
import numpy as np
import os
import fnmatch
from skimage import io


class dataLoader:
    """
    This module load the data to the memory of local machine.
    Data is in the file of local machine, which is fetch from the remote    
    """

    def __init__(self, copier: SFTP_copier) -> None:
        """
        Initialize the SFTPClient object that is used for file transporting
        """
        self.copier = copier


    def list_dir(self, remote_path: str, format: str) -> str:
        """
        Return first path in list containing all files (full path) in "remote_path" of the "format"

        format: /*_{:04d}_depth.npy'

        Mimic the functionality of glob.glob
        """

        output = []

        for filename in self.copier.sftp.listdir(remote_path):
            
                filePath = os.path.join(remote_path, filename)
                output.append(filePath)
        
        return output[0]


    def dvsLoader(self, filepath: str, localPath: str) -> np.array:
        """
        Load the *.npy file of DVS camera into numpy array
        """
       
        fullpath_local = self.copier.data_retriver(filepath, localPath, localpath_alreadyFILE=False)

        output = np.load(fullpath_local)

        # load data to mem, delete the file in the folder
        os.system('rm %s' % fullpath_local)

        return output


    def timestampLoader(self, filePath: str, localPath: str) -> np.ndarray:
        """
        Load the timestamp file

        filePath: /timestamps.txt
        """

        if fnmatch.fnmatch(filePath, '*.txt'):

            fullpath_local = self.copier.data_retriver(filePath, localPath, localpath_alreadyFILE=False) 
            # auto handle connection in data_retriver

            output = np.loadtxt(fullpath_local)

            # load data to mem, delete the file in the folder
            os.system('rm %s' % fullpath_local)

            return output

        else:
            raise("timestamps.txt name error")



    def depthFrameLoader(self, filePath: str, localPath: str) -> np.array:
        """
        Load the *.npy file of depth camera into a numpy array

        filePath: remote full path of the file
        """

        fullpath_local = self.copier.data_retriver(filePath, localPath, localpath_alreadyFILE=False) 
        # auto handle connection in data_retriver

        output = np.load(fullpath_local).astype(np.float32)

        # load data to mem, delete the file in the folder
        os.system('rm %s' % fullpath_local)

        return output


    def rgbReader(self, filePath: str, localPath: str) -> np.ndarray:
        """
        Read the rgb image into a ndarray 
        """

        fullpath_local = self.copier.data_retriver(filePath, localPath, localpath_alreadyFILE=False)

        rgb_frame = io.imread(fullpath_local, as_gray=False).astype(np.float32)

         # load data to mem, delete the file in the folder
        os.system('rm %s' % fullpath_local)

        return rgb_frame
        

# if __name__ == '__main__':

#     # test for the connection of the SFTP channel
#     copier = SFTP_copier()
#     loader = dataLoader(copier)

#     # test list_dir function
#     remote_path = '/SCRATCH/project/data/training/full_data/Town03_sequence_89/depth/data'
#     local_dir =  '/h/sankeert/zhonghan_chen/trainer/RAM_Net/SFTP_Solver/experiment'
#     format = '*_depth.npy'
#     filepath = loader.list_dir(remote_path, format)

#     # test depthFrameLoader by the shape
#     realdata = loader.depthFrameLoader(filepath, local_dir)
#     print("the shape of the npy file is:", np.shape(realdata))


#     # test rgbReader by the shape of the output
#     remote_path = '/SCRATCH/project/data/training/full_data/Town03_sequence_89/rgb/data'
#     local_dir =  '/h/sankeert/zhonghan_chen/trainer/RAM_Net/SFTP_Solver/experiment'
#     format = '*png'
#     filepath = loader.list_dir(remote_path, format)

#     print("remote file path:", filepath)

#     realdata = loader.rgbReader(filepath, local_dir)
#     print("the shape of the array is:", np.shape(realdata))


#     # test dvsLoader by the shape of the output
#     remote_path = '/SCRATCH/project/data/training/full_data/Town03_sequence_89/events/voxels'
#     local_dir =  '/h/sankeert/zhonghan_chen/trainer/RAM_Net/SFTP_Solver/experiment'
#     format = '*npy'
#     filepath = loader.list_dir(remote_path, format)

#     # print("remote file path:", filepath)

#     realdata = loader.dvsLoader(filepath, local_dir)
#     print("the shape of the npy file is:", np.shape(realdata))


#     # test timestampLoader by the shape of the output
#     remote_path = '/SCRATCH/project/data/training/full_data/Town03_sequence_89/events/voxels/timestamps.txt'
#     local_dir =  '/h/sankeert/zhonghan_chen/trainer/RAM_Net/SFTP_Solver/experiment'

#     realdata = loader.timestampLoader(remote_path, local_dir)
#     print("the shape of the array is:", np.shape(realdata))

   



