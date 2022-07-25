# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    cocotb.log.info(f'answer={dut.current_state.value}')
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    cocotb.log.info(f'answer={dut.current_state.value}')

    cocotb.log.info('#### CTB: Develop your test here! ######')
    cocotb.log.info('helloo hi')
    print("hi uc")
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'answer={dut.current_state.value} output={dut.seq_seen.value}')
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'answer={dut.current_state.value} output={dut.seq_seen.value}')
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    cocotb.log.info(f'answer={dut.current_state.value} output={dut.seq_seen.value}')
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'answer={dut.current_state.value} output={dut.seq_seen.value}')
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'answer={dut.current_state.value} output={dut.seq_seen.value}')
    assert dut.seq_seen.value==1,"bug for input stream identified {input}".format(input=11011)

    # cocotb.log.info(f'answer={dut.current_state.value} output ={dut.seq_seen.value}')