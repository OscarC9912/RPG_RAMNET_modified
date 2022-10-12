## My Modification To the Project

Base on the RPG_RAMNET at University of Zurich

Link to original project: `https://github.com/uzh-rpg/rpg_ramnet`

### **SFTP_Solver**:
The folder is used to establish the connection between @mel and @vector to transport the data for training. And it is a helper folder for the Dataloader

##### **SFTP_Solver/copier.py**: 
Set up the connection and provide function that transport the data

##### **SFTP_Solver/dataLoader.py**:
Load different types of data including DVS, Depth, RGB

##### **SFPT_Solver/connector.py**:
A simple python script that sets up the connection, which uses both previous scripts


### **configs:**:

Added storage_path.json, which specifies the local absolute path that temporily stores data retrived from the remote machine.


### **data_loader_copy**:

The folder is a backup for the orginal data loaders of the project.


[![name](https://github.com/uzh-rpg/rpg_ramnet/raw/master/doc/img/RAM_Net_preview.png)
