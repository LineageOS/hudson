# Accessing the Build Server
http://n0.clockworkmod.com:9999/ (will eventually move to a CM subdomain)

# Authenticating to the Build Server
You must be a member of the CyanogenMod organization.

Your username and password is your Github username and Github API Token.  
Your API token is accessible here:  
https://github.com/settings/admin  

You must also make sure your CyanogenMod membership is not concealed. You can do that here:  
https://github.com/CyanogenMod  

# Using the Build Server
Click the "android" job.  
Configure what you want to build.  
Build it.  

# Modifying the local_manifest.xml
Edit ics.xml (the ics local_manifest.xml) and submit a pull request.  
Or edit gingerbread.xml (the gingerbread local_manifest.xml) and submit a pull request.  

# Adding Nodes to the Build Server
More nodes the better.  
To add a node, please open an issue with a externally accessible username and host name that Hudson can use to connect via SSH.  
Your build machine must also be completely/properly set up to support building Android. sudo/root access is not required.  

The login provided should use allow access to the following public key via the authorized_keys file:  
https://github.com/CyanogenMod/hudson/blob/master/authorized_keys  