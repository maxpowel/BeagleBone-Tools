serialPorts = {"/dev/ttyO1":
			{"uart1_rxd": "20",
			 "uart1_txd": "0"
			},
		"/dev/ttyO2":
			{"spi0_sclk": "21",
			 "spi0_d0": "1"
			},
		"/dev/ttyO4":
			{"gpmc_wait0": "26",
			 "gpmc_wpn": "6"
			},
		"/dev/ttyO5":
			{"lcd_data9": "24",
			 "lcd_data8": "4"
			}
		}

def enable(portName):
	if not portName in serialPorts:
		raise Exception('Port ' + portName + ' does not exists')
	else:	
		for name in serialPorts[portName]:
			open('/sys/kernel/debug/omap_mux/' + name, 'w').write(serialPorts[portName][name])
