The verification environment is setup using Vyoma's UpTickPro provided for the hackathon

```screenshot of gitpod environment ```
![Screenshot (35)](https://user-images.githubusercontent.com/77403373/180925890-8932e808-45cd-43ae-b2ae-767de5f0f3ad.png)

## Verification Environment
The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (multiplexer module here) which takes in 5-bit input *sel* and 2-bit inputs from *inp1 to inp29* and gives 2-bit output *out*

The values are assigned to the input port using 
```
dut.inp1.value,dut.inp3.value,dut.inp5.value,dut.inp7.value,dut.inp9.value,dut.inp11.value,dut.inp13.value,dut.inp15.value,dut.inp17.value,dut.inp19.value,dut.inp21.value,dut.inp23.value,dut.inp25.value,dut.inp27.value,dut.inp29.value=1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
dut.inp0.value,dut.inp2.value,dut.inp4.value,dut.inp6.value,dut.inp8.value,dut.inp10.value,dut.inp12.value,dut.inp14.value,dut.inp16.value,dut.inp18.value,dut.inp20.value,dut.inp22.value,dut.inp24.value,dut.inp26.value,dut.inp28.value,dut.inp30.value=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
```
Here inputs are assigned as for odd ports as 1 and for even ports as 0

The assert statement is used for comparing the mux's outut to the expected value.

The following error is seen:

