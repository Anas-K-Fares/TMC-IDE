clear;
clc;
close all;

[status devs]=system("py -3 Network_client.py lstmc")

devsS=convertCharsToStrings(devs(2:(end-2)))
devs=jsondecode("["+devsS.replace("'", '"')+"]")

myScopeDesc=split(devs(1),"::")
myScope=cell2mat(myScopeDesc(1))
myScopeIdn=cell2mat(myScopeDesc(2))

[status dataC]=system("py -3 Network_client.py "+myScope+"::iwav:data?");

dataS=convertCharsToStrings(dataC(2:end-2));

data=str2double(split(dataS,','));

plot(data)
