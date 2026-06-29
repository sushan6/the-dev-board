# The Dev Board

This repository contains the design files for a custom microcontroller development board built using KiCad. The project centers around the RP2040 chip, breaking out its pins and incorporating essential subsystems for power, storage, and external connectivity.

## Project Overview

This development board is designed to be a compact, reliable prototyping platform using the RP2040 microcontroller. It handles power management, high-speed external memory routing, and precise clocking, making it ready for custom embedded software applications.

## Key Features

* Microcontroller: Based on the RP2040 chip, bringing twin core processing capabilities to a custom hardware layout.
* Power Management: Driven by a modern USB C receptacle for both power delivery and data interfacing, regulated down to a clean three point three volts using an onboard linear regulator.
* External Storage: Incorporates external flash memory connected over a quad serial peripheral interface, giving ample room for large programs and data storage.
* Clock Source: Utilizes a twelve megahertz crystal oscillator circuit to ensure stable and highly accurate clock timing for the microcontroller.
* Input and Output Breakouts: Exposes general purpose input output pins to dual row pin headers, providing quick access for connecting sensors, displays, and external components.

## Hardware Design and Previews

### Schematic Layout
The schematic is divided into clean functional blocks including power management, flash memory wiring, crystal clock generation, and pin mappings. 

<img width="817" height="579" alt="image" src="https://github.com/user-attachments/assets/6711d180-5367-4b4c-a65a-19ef6d6183bf" />

---

### PCB Layout and 3D Visualizations
The physical layout focuses on tight trace routing, proper decoupling capacitor placement for power stability, and optimized signal paths. 
<img width="210" height="409" alt="pcb image" src="https://github.com/user-attachments/assets/d244f31b-1b99-4f67-ad2c-be14d9a364b1" />

#### Board Front View
<img width="302" height="599" alt="front-3d-pcb" src="https://github.com/user-attachments/assets/540ede24-c20b-4fff-8cf0-4c68a771e3ca" />


#### Board Back View
<img width="288" height="582" alt="back-3d-pcb" src="https://github.com/user-attachments/assets/b0ab2e89-41ff-4279-a087-f5cc453e1552" />
