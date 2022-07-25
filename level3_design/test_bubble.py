# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_bubble_bug1(dut):
    
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    await FallingEdge(dut.clk)
    dut.in1.value = 5
    await FallingEdge(dut.clk)
    dut.in2.value = 4
    await FallingEdge(dut.clk)
    dut.in3.value = 3
    await FallingEdge(dut.clk)
    dut.in4.value = 2
    await FallingEdge(dut.clk)
    dut.in5.value = 1
    await FallingEdge(dut.clk)
    cocotb.log.info('dut.in1.value {j}'.format(j=dut.in1.value))
    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)
    assert (dut.out1.value==1),"ERROR IN SORTING1"
    assert (dut.out2.value==2),"ERROR IN SORTING2"
    assert (dut.out3.value==4),"ERROR IN SORTING3"
    assert (dut.out4.value==3),"ERROR IN SORTING4"
    assert (dut.out5.value==5),"ERROR IN SORTING5"
    