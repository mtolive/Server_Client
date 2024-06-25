Running a Server Program on VxWorks 7 in QEMU (x86)
This repository contains a simple server program designed to run on VxWorks 7 within the QEMU x86 emulator. The client script provided was tested on WSL but can be used in any local terminal environment.

Getting Started
VxWorks 7 SDK for QEMU (x86)
To set up the development environment, you'll need the VxWorks 7 Software Development Kit (SDK) for QEMU (x86).

Installation Steps:
Dependencies on Debian-based Systems:

```
sudo apt update
sudo apt install build-essential libc6-i386
sudo apt install python-pip
sudo pip install pyftpdlib
```
Download and Setup VxWorks 7 SDK:

You can download the SDK from Wind River's official forum or use the direct download link:

VxWorks 7 SDK for QEMU (x86) Version 1.14
Extract the SDK and set up the development environment:

```
tar -xvf wrsdk-vxworks7-qemu-1.14.tar.bz2
cd wrsdk-vxworks7-qemu-1.14
source sdkenv.sh
```

Compile and Run the Server Program

Compile your server program (server.c) using the Wind River compiler (wr-cc):
```
wr-cc -rtp server.c -static -o server.vxe
```
Start VxWorks 7 in QEMU with the following command:
```
qemu-system-x86_64 -m 512M -kernel vxsdk/bsps/itl_generic_3_0_0_4/vxWorks \
-net nic -net user,hostfwd=tcp::1534-:1534,hostfwd=tcp::2345-:2345,hostfwd=tcp::18000-:18000 \
-display none -serial stdio -monitor none \
-append "bootline:fs(0,0)host:vxWorks h=10.0.2.2 e=10.0.2.15 u=target pw=vxTarget o=gei0"
```
Note: Adjust the port forwarding (hostfwd=tcp::18000-:18000) to match the port used in your server.c if necessary.

Running an FTP Server
Start an FTP server on port 21 in another terminal to facilitate file transfer:

```
sudo python -m pyftpdlib -p 21 -u target -P vxTarget -d $HOME &
```
Sharing Files with QEMU
Create a shared directory and move your server.vxe file there:

```
mkdir -p ~/opt
mv server.vxe ~/opt
```
In the QEMU terminal, switch to the command shell and navigate to the shared directory:

```
cmd
cd opt
ls
```
Running the Server and Client
Finally, start your server program (server.vxe) in the QEMU terminal and run the client script (client.py) in a third terminal:

```
server.vxe
```
```
python3 client.py
```
This setup should enable you to run and test your server program on VxWorks 7 in QEMU with ease. For more detailed information, refer to the official README from Wind River.
