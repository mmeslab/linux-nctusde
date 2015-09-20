#!/usr/bin/python

nctuss_symbol_names = ["nctuss_poll_emacps",
					"nctuss_xemacps_tx_poll",
					"xemacps_tx_hwtstamp",
					"nctuss_xemacps_rx",
					"nctuss_xemacps_send_skb",
					"nctuss_xemacps_start_xmit",
					"xemacps_clear_csum",
					"nctuss_xemacps_return_skb",
					"nctuss_skb_pool_return",
					"nctuss_gt_stop",
					"nctuss_gt_resume",
					"nctuss_gt_get_gt_counter_base",
					"nctuss_gt_get_counter_value",
					"nctuss_ttc_stop",
					"nctuss_ttc_resume",
					"nctuss_smp_invoke_function",
					#"wakeup_softirqd",
					"skb_push",
					"skb_reset_transport_header", # inline function
					"udp_hdr", # inline function
					"skb_reset_network_header", # inline function
					"skb_reset_mac_header", # inline function
					"skb_reserve", # inline function
						]

if __name__ == '__main__':
	f = open("System.map", "r")

	totalSize = 0
	symbolNamesFound = 0

	lines = f.readlines()
	for i in range(0, len(lines)):
		line = lines[i]
		
		symbol_name = line[11:-1]

		if symbol_name in nctuss_symbol_names:
			print symbol_name
			
			address = int(line[0:8], 16)
			addressNext = int(lines[i+1][0:8], 16)

			size = addressNext - address
			
			totalSize += size
			symbolNamesFound += 1

	print "totalSize: %s" % (totalSize)
	print "symbolNamesFound: %s" % (symbolNamesFound)


	f.close()

