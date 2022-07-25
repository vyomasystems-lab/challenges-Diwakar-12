# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_bubble_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    
    dut.in1.value = 5 
    dut.in2.value = 4
    dut.in3.value = 3
    dut.in4.value = 2
    dut.in5.value = 1
    
    
    assert (dut.out1.value==1)&&(dut.out2.value==2)&&(dut.out3.value==3)&&(dut.out4.value==4)&&(dut.out5.value==5),"ERROR IN SORTING"