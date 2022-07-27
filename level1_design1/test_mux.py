# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    
    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp1.value,dut.inp3.value,dut.inp5.value,dut.inp7.value,dut.inp9.value,dut.inp11.value,dut.inp13.value,dut.inp15.value,dut.inp17.value,dut.inp19.value,dut.inp21.value,dut.inp23.value,dut.inp25.value,dut.inp27.value,dut.inp29.value=1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
    dut.inp0.value,dut.inp2.value,dut.inp4.value,dut.inp6.value,dut.inp8.value,dut.inp10.value,dut.inp12.value,dut.inp14.value,dut.inp16.value,dut.inp18.value,dut.inp20.value,dut.inp22.value,dut.inp24.value,dut.inp26.value,dut.inp28.value,dut.inp30.value=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    for i in range(0,31):
        A = i

        # input driving
        dut.sel.value = A


        await Timer(2, units='ns')
        dut._log.info(f'A={A:05} model={A%2:02} DUT={int(dut.out.value):02}')
        assert dut.out.value == i%2,"failed for input select line {v},expected is {v1}".format(v=i,v1=i%2)
