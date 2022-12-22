ROP_POPJUMPLR_STACK12 = 0x0101CD24
ROP_POPJUMPLR_STACK20 = 0x01024D88
ROP_CALLFUNC = 0x01080274
ROP_CALLR28_POP_R28_TO_R31 = 0x0107DD70
ROP_POP_R28R29R30R31 = 0x0101D8D4
ROP_POP_R27 = 0x0101CB00
ROP_POP_R24_TO_R31 = 0x010204C8
ROP_CALLFUNCPTR_WITHARGS_FROM_R3MEM = 0x010253C0
ROP_SETR3TOR31_POP_R31 = 0x0101CC10
ROP_Register = 0x010277B8
ROP_CopyToSaveArea = 0x010277DC
ROP_memcpy = 0x01035FC8
ROP_DCFlushRange = 0x01023F88
ROP_ICInvalidateRange = 0x010240B0
ROP_OSSwitchSecCodeGenMode = 0x010376C0
ROP_OSCodegenCopy = 0x010376D8
ROP_OSGetCodegenVirtAddrRange = 0x010375C0
ROP_OSGetCoreId = 0x01024E8C
ROP_OSGetCurrentThread = 0x01043150
ROP_OSSetThreadAffinity = 0x010429DC
ROP_OSYieldThread = 0x010418E4
ROP_OSFatal = 0x01031618
ROP_Exit = 0x0101CD80
ROP_OSScreenFlipBuffersEx = 0x0103AFD0
ROP_OSScreenClearBufferEx = 0x0103B090
ROP_OSDynLoad_Acquire = 0x0102A3B4
ROP_OSDynLoad_FindExport = 0x0102B828
ROP_os_snprintf = 0x0102F160
ROP_GX2Init = 0x01156B78
ROP_GX2Flush = 0x011575AC
ROP_GX2WaitForVsync = 0x01151964
ROP_GX2DirectCallDisplayList = 0x01152BF0
ROP_GXCallDisplayList = 0x01152B3C

ROP_DCStoreRange = 0x02007BC4 - 0xFE3C00
ROP_IOS_Open = 0x0203246C - 0xFE3C00
ROP_Restart = 0x02019A80 - 0xFE3C00
ROP_OSDriver_Register = 0x010277B8
ROP_OSDriver_Deregister = 0x010277C4
ROP_OSDriver_CopyFromSaveArea = 0x010277D0
ROP_OSDriver_CopyToSaveArea = 0x010277DC
ROP_OSBlockMove = 0x02019EE4 - 0xFE3C00
ROP_OSExitThread = 0x0202596C - 0xFE3C00 
ROP_memset = 0x02019BB4 - 0xFE3C00
ROP_memclr = 0x02019BBC - 0xFE3C00
ROP_OSSendAppSwitchRequest = 0x0201D830 - 0xFE3C00
ROP_Syscall_0x01 = 0x02014A5C - 0xFE3C00