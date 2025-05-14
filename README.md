# Artificer A1 Single Board Computer
 An open source single board computer with AI capabilities. (Still in progress)

 ![SBC IMG](https://github.com/MattSpot10/Artificer-A1-Single-Board-Computer/blob/main/_images/Atificer%20A1%20PCB%20layout%20next%20to%20raspberry%20pi%204.jpg)

### **Features/Capabilites
- Alliwnner T527 SoC (Octa-core ARM Cortex-A55, up to 1.8 GHz)
- 4GB LPDDR4 SDRAM
- Dual Gigibit Ethernet (RJ45 ports capable of PoE)
- PCIe gen 2.1
- Display Port, HDMI, 2x4 lane MIPI DSI
- 4x2 lane MIPI CSI
- SD Card as boot media
- M8800DS2 Wifi/BT module with onboard PCB antenna
- 12V 5.5mm barrel jack power input
- 2x20 raspberry pi GPIO header
- 3.5mm sterio audio, mic
- 4xUSBA 2.0
- 1xUSBC 2.0 DRD

### **Progress/Plans (Since Jan 2025)**
**V1 Schematic capture**
- Done: Component choice, symbol, and footprint creation. Finished interconnects for Ethernet, USB, MIPI DSI & CSI, SDRAM, PCIe
- Todo: Interconnects for power, audio, gpio, I2C interfaces, wifi&bt, SD card.
![Hierarchical schematic](https://github.com/MattSpot10/Artificer-A1-Single-Board-Computer/blob/main/_images/Hierarchical%20schematic.jpg)

**PCB Compatabilites**

The Allwinner T527 is a 0.5mm pitch BGA requiring these compatabilities for maufacturing:
- 3mil trace
- 3mil spacing
- 10.685mil pad
- 6mil drill
- 10.685mil pad - 6mil drill = 2.342mil anular ring
- 6 - 8 layers (Stackup and material not determined)

**Booting Linux**
- Add Spi flash chip to schematic for holding U Boot.
- Configure U Boot for loading the Linux kernel and the device tree blob.
