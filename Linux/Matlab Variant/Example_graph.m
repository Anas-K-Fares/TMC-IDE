clear;
clc;
close all;

libPath="'."
[status devs]=system("python3 "+libPath+"/Network_client.py' lstmc")

devsS = convertCharsToStrings(devs(2:(end-2)))
devsList = jsondecode("["+devsS.replace("'", '"')+"]")

myScopeDesc = split(devsList(1),"::")
myScope = cell2mat(myScopeDesc(1))
myScopeIdn = cell2mat(myScopeDesc(2))

[status dataC] = system("python3 "+libPath+"/Network_client.py' "+myScope+"::iwav:data?");

dataS = convertCharsToStrings(dataC(2:end-2));

data = str2double(split(dataS,','));

plot(data)
