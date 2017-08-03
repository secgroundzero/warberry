"""
This file is part of the WarBerry tool.
Copyright (c) 2016 Yiannis Ioannides (@sec_groundzero).
https://github.com/secgroundzero/warberry
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""

class port_ob:

    path_file=""
    result_file=""
    message=""
    name=""
    port = []
    scan_type=""

    #CONSTRUCTOR
    def __init__(self, pf, rf,mess,na,por, st):
        self.path_file=pf
        self.result_file=rf
        self.message=mess
        self.name=na
        port_list = []
        #check if there are multiple ports
        if '.' in por:
            port_nums=por.split('.')
            for p in port_nums:
                port_list.append(p)
        else:
            port_list.append(por)
        self.port=port_list
        self.scan_type=st

    #GETTER FUNCTION
    def getatt(self,num):
        if num==0:
            return self.path_file
        elif num==1:
            return self.result_file
        elif num==2:
            return self.message
        elif num==3:
            return self.name
        elif num==4:
            return self.port
        else: return self.scan_type