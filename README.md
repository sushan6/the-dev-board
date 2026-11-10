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

## Bill of Materials (BOM)

### Main BOM

| **Item** | **Link** | **Quantity** | **Cost (USD)** |
|---|---|---:|---:|
| 1 µF Capacitors (0402) | [Robu.in](https://robu.in/product/1uf-capacitor-smdc-0402-pack-of-50/) | 20 | $0.06 |
| 100 nF Capacitors (0402) | [Robu.in](https://robu.in/product/0402b104j250nt-fh-25v-100nf-x7r%C2%B15-0402-multilayer-ceramic-capacitors-mlcc-smd-smt-rohs/) | 20 | $0.14 |
| 10 µF Capacitors (0603) | [Robu.in](https://robu.in/product/0603x106m100nt-fh-10v-10uf-x5r%C2%B120-0603-multilayer-ceramic-capacitors-mlcc-smd-smt-rohs/) | 20 | $0.53 |
| 33 pF Capacitors (0402) | [Robu.in](https://robu.in/product/0402cg330j160nt-fh-smd-multilayer-ceramic-capacitor-33-pf-16-v-0402-1005-metric-%25c2%25b1-5-c0g-np0/) | 20 | $0.01 |
| USB-C Receptacles | [LCSC India](https://lcscindia.com/part/TYPE-C-31-M-12) | 2 | $0.45 |
| 1×20 Pin Headers | [Robu.in](https://robu.in/product/ds1021-1x20sf11-b-connfly-1x20-pin-2-54mm-pin-header-v-t-type/) | 4 | $0.55 |
| MicroSD Card Connectors | [RS India](https://in.rsdelivers.com/product/molex/104031-0811/molex-104031-8-way-push-pull-microsd-memory-card/8967560) | 2 | $4.68 |
| 5.1 kΩ Resistors (0402) | [Robu.in](https://robu.in/product/rc0402fr-075k1l-yageo-res-thick-film-0402-5-1k-ohm-1-0-063w1-16w-%C2%B1100ppm-c-pad-smd-t-r/) | 20 | $0.05 |
| 27 Ω Resistors (0402) | [Robu.in](https://robu.in/product/rc0402jr-0727rl-yageo-res-thick-film-0402-27-ohm-5-0-063w1-16w-%25c2%25b1100ppm-c-pad-smd-t-r/) | 20 | $0.02 |
| 1 kΩ Resistors (0402) | [Robu.in](https://robu.in/product/rc0402fr-071kl-yageo-res-thick-film-0402-1k-ohm-1-0-063w1-16w-%C2%B1100ppm-c-pad-smd-t-r/) | 20 | $0.03 |
| 10 kΩ Resistors (0402) | [Robu.in](https://robu.in/product/10k-resistor-smdr-0402-pack-of-50/) | 20 | $0.07 |
| Tactile Switches | [Robu.in](https://robu.in/product/tsa010a2026b-bzcn-3mm-2mm-50ma-round-button-standing-paste-3-9mm-260gf-12v-smd-tactile-switches-rohs/) | 2 | $0.04 |
| RP2040 Microcontrollers | [Robocraze](https://robocraze.com/products/raspberry-pi-rp2040-microcontroller-ic-chip) | 2 | $1.36 |
| 3.3V Voltage Regulators | [Microchip](https://www.microchip.com/en-us/product/MCP1700) | 2 | $1.20 |
| 16 Mbit SPI Flash | [Lion Circuits](https://www.lioncircuits.com/parts/W25Q16JVUXIQ%20TR) | 2 | $4.88 |
| 12 MHz Crystals | [Robu.in](https://robu.in/product/ysx321sl-12mhz-12pf-10ppm-4pins-smd-smt-metal-surface-quartz-crystal-pack-of-2/) | 2 | $0.43 |
| Soldering Starter Kit | [Robu.in](https://robu.in/product/soldering-starter-tool-kit-30w-iron-solder-sponge/) | 1 | $13.30 |
| Custom PCB | [JLCPCB](https://jlcpcb.com/) | 2 | $15.00 |

### Cost Summary

| **Item** | **Cost (USD)** |
|---|---:|
| Capacitors (20 each) | $0.75 |
| Resistors (20 each) | $0.16 |
| USB-C Receptacles | $0.45 |
| 1×20 Pin Headers | $0.55 |
| MicroSD Connectors | $4.68 |
| Tactile Switches | $0.04 |
| RP2040 Microcontrollers | $1.36 |
| Voltage Regulators | $1.20 |
| SPI Flash Memory | $4.88 |
| 12 MHz Crystals | $0.43 |
| Soldering Starter Kit | $13.30 |
| PCB Fabrication | $15.00 |
| **Total** | **$42.80** |

Note: Some items are ordered in multipe quantity because of minimum order value
