# Sushan's dev board 

This development board is designed to be a compact, reliable prototyping platform using the RP2040 microcontroller. It handles power management, high-speed external memory routing, and precise clocking, making it ready for custom embedded software applications.

## Key Features

* Microcontroller: Based on the RP2040 chip, bringing twin-core processing capabilities to a custom hardware layout.
* Power Management: Driven by a modern USB-C receptacle for both power delivery and data interfacing, regulated down to a clean three-point-three volts using an onboard linear regulator.
* External Storage: Incorporates external flash memory connected over a quad serial peripheral interface, giving ample room for large programs and data storage.
* Clock Source: Utilises a twelve megahertz crystal oscillator circuit to ensure stable and highly accurate clock timing for the microcontroller.
* Input and Output Breakouts: Exposes general-purpose input/output pins to dual-row pin headers, providing quick access for connecting sensors, displays, and external components.
* There are 40 pins externally for data
* SD card reader 
## Hardware Design and Previews

### Schematic Layout
The schematic is divided into clean functional blocks including power management, flash memory wiring, crystal clock generation, and pin mappings. 

<img width="738" height="520" alt="schematics1" src="https://github.com/user-attachments/assets/5eee4fdb-c5f1-40e2-8ffe-b2b7f1e71cac" />

---

### PCB Layout and 3D Visualisations
The physical layout focuses on tight trace routing, proper decoupling capacitor placement for power stability, and optimised signal paths. 

<img width="298" height="406" alt="pcb image1" src="https://github.com/user-attachments/assets/4f1341b9-f3c7-47d9-a2a1-7af2dd44f1b4" />


#### Board Front View

<img width="308" height="563" alt="front-3d-pcb1" src="https://github.com/user-attachments/assets/ddfaa523-9028-4dc1-951d-6c2c8d5300e6" />



#### Board Back View

<img width="358" height="561" alt="back-3d-pcb1" src="https://github.com/user-attachments/assets/a001488e-4d79-4d8a-b426-7ab197211070" />
