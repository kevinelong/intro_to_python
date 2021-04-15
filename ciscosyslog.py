text = """
*Mar  1 00:00:01.137: %VIRTIO-3-INIT_FAIL: Failed to initialize device, PCI 0/6/0/1002 , device is disabled, not supported
*Mar  1 00:00:01.381: %ATA-6-DEV_FOUND: device 0x1F0
*Mar  1 00:00:08.485: %ATA-6-DEV_FOUND: device 0x171
*Mar  1 00:00:08.704: %NVRAM-5-CONFIG_NVRAM_READ_OK: NVRAM configuration 'flash:/nvram' was read from disk.
*Feb  8 08:51:58.706: %PA-3-PA_INIT_FAILED: Performance Agent failed to initialize (Missing Data License)
*Feb  8 08:52:05.064: %LINK-3-UPDOWN: Interface GigabitEthernet0/0, changed state to up
*Feb  8 08:52:05.068: %LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to up
*Mar  2 00:00:01.137: %VIRTIO-3-INIT_FAIL: Failed to initialize device, PCI 0/6/0/1002 , device is disabled, not supported
*Mar  2 00:00:01.381: %ATA-6-DEV_FOUND: device 0x1F0
*Mar  2 00:00:08.485: %ATA-6-DEV_FOUND: device 0x171
*Mar  2 00:00:08.704: %NVRAM-5-CONFIG_NVRAM_READ_OK: NVRAM configuration 'flash:/nvram' was read from disk.
*Feb  9 08:51:58.706: %PA-3-PA_INIT_FAILED: Performance Agent failed to initialize (Missing Data License)
*Feb  9 08:52:05.064: %LINK-3-UPDOWN: Interface GigabitEthernet0/0, changed state to up
*Feb  9 08:52:05.068: %LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to up
*Mar  3 00:00:01.137: %VIRTIO-3-INIT_FAIL: Failed to initialize device, PCI 0/6/0/1002 , device is disabled, not supported
*Mar  3 00:00:01.381: %ATA-6-DEV_FOUND: device 0x1F0
*Mar  3 00:00:08.485: %ATA-6-DEV_FOUND: device 0x171
*Mar  3 00:00:08.704: %NVRAM-5-CONFIG_NVRAM_READ_OK: NVRAM configuration 'flash:/nvram' was read from disk.
*Feb  11 08:51:58.706: %PA-3-PA_INIT_FAILED: Performance Agent failed to initialize (Missing Data License)
*Feb  11 08:52:05.064: %LINK-3-UPDOWN: Interface GigabitEthernet0/0, changed state to up
*Feb  11 08:52:05.068: %LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to up
"""

"""
timestamp: Feb 14 0:40:10.326
facility: %LINEPROTO
severity level: 5
mnemonic: UPDOWN
description: Line protocol on Interface GigabitEthernet0/1, changed state to up
"""

FACILITY_SEVERITY_MNEMONIC_INDEX = 3

line_list = text.split("\n")
pa_failure_count = 0
for line in line_list:
    if line.strip() == "":
        continue  # go to the top and to the next item if there is one
    parts = line.split()  # pass in no separator split on whitespace

    facility_severity_mnemonic = parts[FACILITY_SEVERITY_MNEMONIC_INDEX]
    facility_severity_mnemonic = facility_severity_mnemonic[1:-1] # skip first and last characters

    # pieces = facility_severity_mnemonic.split("-")
    # facility = pieces[0]
    # severity = pieces[1]
    # mnemonic = pieces[2]

    facility, severity, mnemonic = facility_severity_mnemonic.split("-") # UNPACK THE LIST INTO THREE VARS
    severity = int(severity)
    if severity > 0:
        if "fail" in mnemonic.lower():
            if "PA" == facility.upper():
                print(mnemonic)
                # pa_failure_count = pa_failure_count + 1  #  TOO LONG BUT WOULD WORK
                pa_failure_count += 1
                # pa_failure_count++  #  NOPE - nopt int PYTHON
print(pa_failure_count)
