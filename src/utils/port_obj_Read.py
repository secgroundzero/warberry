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

import port_object

"""this function is used to read portlist_config file and create
the port object list with port characteristic properties."""
def port_obj_reader(filename):
    ports_obj_list = []
    with open('src/core/scanners/portlist_config','r') as ports_input_file:
        for line in ports_input_file:
            f=line.split(',')
            s=f[5]     #this is to get only y/n not \n
            f[5]=s[0]   #this is to get only y/n not \n
            portOB = port_object.port_ob(f[0],f[1],f[2],f[3],f[4],f[5])
            ports_obj_list.append(portOB)
    return ports_obj_list