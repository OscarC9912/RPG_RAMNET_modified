"""
The file contains the module that connect to the SFTP and copy the data accordingly.
"""

import paramiko  # the library that support SFTP agreement
import os


class SFTP_copier:
    """
    SFTP_copier Class contains function transferring files between ssh server
    """

    def __init__(self) -> None:
        """
        Initialize the object, so that we are able to use add function to it.
        """

        # connect to the cslab server first
        conn_lab = paramiko.SSHClient()
        conn_lab.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conn_lab.connect('syslab.cs.toronto.edu', port=22, username='sankeerth', timeout=700)

        # set up the transport channel between mel and cslab server
        labTransport = conn_lab.get_transport()
        local_addr = ('syslab.cs.toronto.edu', 22)
        dest_addr = ('mel-15', 22)
        labchannel = labTransport.open_channel("direct-tcpip", dest_addr, local_addr)

        # connect to the mel machine in cslab
        mel = paramiko.SSHClient()
        mel.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        mel.connect('mel-15', port=22, username='chen', sock=labchannel, timeout=700)

        # set up an SFTP client object
        sfpt_obj = mel.open_sftp()

        self.sftp = sfpt_obj


    def data_retriver(self, remote_path: str, local_path: str, localpath_alreadyFILE: bool) -> str:
        """
        Copy the file of remote machine @mel to local machine @ vector and return full path of file (local)

        remote_path: full directory of remote file
        local_path: the file path / the directory path in local machine
        localpath_alreadyFILE: true iff local path contains file name
        """
        
        if localpath_alreadyFILE:  # the case when local_path contains file name
            self.sftp.get(remote_path, local_path, callback=None, prefetch=True)
        else:
            local_file_path = self._path_generator(remote_path, local_path)
            self.sftp.get(remote_path, local_file_path, callback=None, prefetch=True)
            return local_file_path


    def _path_generator(self, remote_path: str, local_dir_path: str) -> str:
        """
        Helper for data_retriver

            Generate the full path of the file in the local machine, 
            where the name of the remote file and the local file are identical.
        
        remote_file_path: full path of the file in remote machine
        local_dir_path: local directory that will store the new file

        >>> copier = SFTP_copier()
        >>> copier._path_generator('~/dir1/dir2/file1.txt', '~/dir3/dir4')
        '~/dir3/dir4/file1.txt'
        """
        
        splitted = os.path.split(remote_path)

        filename = splitted[1]  # the name of the file

        new_filepath = os.path.join(local_dir_path, filename)

        return new_filepath


 
# if __name__ == '__main__': 
   
#     # testing code 
#     obj = SFTP_copier() 
#     print("type of x", type(obj)) 
#     out = obj.data_retriver('/home/chen/project/try/ramdom.txt',  
#     '/h/sankeert/zhonghan_chen/trainer-activeloop/RAM_Net/SFTP_Solver/experiment/ramdom.txt', True)