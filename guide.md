## Module 1: Exploring YANG Models

#### Task 1 - Open a YANG Model

```
cat models/ietf-interfaces.yang
```
#### Task 2 - Viewing a Standard YANG Model as a Tree

```
pyang -f tree models/ietf-interfaces.yang
```
#### Task 3 - Viewing a Native YANG Model as a Tree

```
pyang -f tree models/Cisco-IOS-XE-platform-software-oper.yang
```

## Module 2: Working with NETCONF
To login to the device via SSH, execute
```
vagrant ssh r1
```

To connect to the device via NETCONF on CLI, execute:  
```
ssh vagrant@localhost -p 2223 -s netconf
```


#### Task 0 - Generate Traffic for Counters
```
cd code
python generate_traffic.py &
```

#### Task 1 - Retrieving Device Configuration with NETCONF
```
python nc_get-config_full.py
```

#### Task 2 - Retrieving Specific Configuration Details with NETCONF
```
python nc_get-config_int.py
```

#### Task 3 - Retrieving Operational Details with NETCONF

```
python nc_get_nat.py
```
#### Task 4 - Edit config (VRF)

```
python nc_edit-config_vrf.py
```
#### Task 5 - Retrieving A Specific XPATH

```
python generate_traffic_xpath.py &
python nc_xpath_nat.py
```

#### Cleanup

```
cd ..
make cleanup
```