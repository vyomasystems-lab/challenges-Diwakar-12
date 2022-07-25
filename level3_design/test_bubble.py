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
    list1=[]
    a=int(input("enter 1st no :"))
    b=int(input("enter 2nd no :"))
    c=int(input("enter 3rd no :"))
    d=int(input("enter 4th no :"))
    e=int(input("enter 5th no :"))
    list1.append(a)
    list1.append(b)
    list1.append(c)
    list1.append(d)
    list1.append(e)
    list1.sort()
    await FallingEdge(dut.clk)
    dut.in1.value = a
    await FallingEdge(dut.clk)
    
    dut.in2.value = b
    await FallingEdge(dut.clk)
    
    dut.in3.value = c
    await FallingEdge(dut.clk)
    
    dut.in4.value = d
    await FallingEdge(dut.clk)
    
    dut.in5.value =e
    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)
    # cocotb.log.info('out1 {l}'.format(l=hex(dut.out1.value)))
    # cocotb.log.info('out2 {l}'.format(l=hex(dut.out2.value)))
    # cocotb.log.info('out3 {l}'.format(l=hex(dut.out3.value)))
    # cocotb.log.info('out4 {l}'.format(l=hex(dut.out4.value)))
    # cocotb.log.info('out5 {l}'.format(l=hex(dut.out5.value)))
    # print(list1)
    assert (dut.out1.value==list1[0]),"ERROR IN SORTING ELEMENTS expected {e5} in position 1 but got {k} ".format(e5=list1[0],k=hex(dut.out1.value))
    assert (dut.out2.value==list1[1]),"ERROR IN SORTING ELEMENTS expected {e5}  in position 2 but got {k}".format(e5=list1[1],k=hex(dut.out2.value))
    assert (dut.out3.value==list1[2]),"ERROR IN SORTING ELEMENTS expected {e5} in position 3 but got {k} ".format(e5=list1[2],k=hex(dut.out3.value))
    assert (dut.out4.value==list1[3]),"ERROR IN SORTING ELEMENTS expected {e5} in position 4 but got {k} ".format(e5=list1[3],k=hex(dut.out4.value))
    assert (dut.out5.value==list1[4]),"ERROR IN SORTING ELEMENTS expected {e5} in position 5 but got {k}".format(e5=list1[4],k=hex(dut.out5.value))
    # (dut.out2.value==2)
    # (dut.out3.value==3)
    # (dut.out4.value==4)
    # (dut.out5.value==5)
