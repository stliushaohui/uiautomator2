# -*- encoding=utf8 -*-
__author__ = "Administrator"
from time import sleep
from airtest.core.api import *
from airtest.cli.parser import cli_setup

from lib.toch_one import Touch_new
if not cli_setup():
    auto_setup(__file__, logdir='./sdk_screen_shots', devices=[
        "Android:///",
    ])
with open('bn_test\\file\\package.txt','r')  as f:
    ap = f.read()

package = ap
print(package)
start_app(package)
# sleep(5)
# stop_app(package)
# start_app(package)
# sleep(5)
t = Touch_new()
# t.toch_new(Template(r"../gjsg_aircase/tpl1579155320530.png", record_pos=(-0.315, 0.091), resolution=(1080, 2280)))
# sleep(8)
# t.toch_new(Template(r"../gjsg_aircase/tpl1579155587095.png", record_pos=(-0.202, 0.29), resolution=(1080, 2280)))
# sleep(5)
# t.toch_new(Template(r"../gjsg_aircase/tpl1579158007949.png", record_pos=(0.002, 0.059), resolution=(1080, 2280)))
# t.toch_new(Template(r"../gjsg_aircase/tpl1579155587095.png", record_pos=(-0.202, 0.29), resolution=(1080, 2280)))
# sleep(2)
# t.toch_new(Template(r"../gjsg_aircase/tpl1579229719400.png", record_pos=(-0.199, 0.17), resolution=(1080, 2280)))
# sleep(2)
t.toch_new(Template(r"../gjsg_aircase/tpl1579155642041.png", record_pos=(0.006, 0.502), resolution=(1080, 2280)))
t.toch_new(Template(r"tpl1581579081392.png", record_pos=(0.001, 0.462), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579090504.png", record_pos=(-0.002, 0.75), resolution=(1080, 2160)))
sleep(5)
t.toch_new(Template(r"tpl1581579121004.png", record_pos=(-0.002, 0.836), resolution=(1080, 2160)))
sleep(3)
t.toch_new(Template(r"tpl1581579144674.png", record_pos=(0.436, 0.915), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579144674.png", record_pos=(0.436, 0.915), resolution=(1080, 2160)))
sleep(2)
t.toch_new(Template(r"tpl1581579182567.png", record_pos=(0.433, 0.915), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579144674.png", record_pos=(0.436, 0.915), resolution=(1080, 2160)))
sleep(2)
t.toch_new(Template(r"tpl1581579203606.png", record_pos=(0.431, 0.911), resolution=(1080, 2160)))
sleep(2)
t.toch_new(Template(r"tpl1581579216914.png", record_pos=(0.437, 0.918), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579216914.png", record_pos=(0.437, 0.918), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579216914.png", record_pos=(0.437, 0.918), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579216914.png", record_pos=(0.437, 0.918), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579216914.png", record_pos=(0.437, 0.918), resolution=(1080, 2160)))
sleep(20)
t.toch_new(Template(r"tpl1581579216914.png", record_pos=(0.437, 0.918), resolution=(1080, 2160)))
sleep(2)
t.toch_new(Template(r"tpl1581579693165.png", record_pos=(0.008, 0.836), resolution=(1080, 2160)))
sleep(2)
t.toch_new(Template(r"tpl1581579707195.png", record_pos=(0.438, 0.912), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579216914.png", record_pos=(0.437, 0.918), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579216914.png", record_pos=(0.437, 0.918), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579731188.png", record_pos=(0.409, 0.529), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579731188.png", record_pos=(0.409, 0.529), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579762833.png", record_pos=(0.184, -0.053), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579762833.png", record_pos=(0.184, -0.053), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579762833.png", record_pos=(0.184, -0.053), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579762833.png", record_pos=(0.184, -0.053), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579786762.png", record_pos=(-0.002, 0.276), resolution=(1080, 2160)))
sleep(2)
t.toch_new(Template(r"tpl1581579796139.png", record_pos=(0.435, 0.917), resolution=(1080, 2160)))
sleep(2)
t.toch_new(Template(r"tpl1581579812991.png", record_pos=(0.401, 0.519), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579812991.png", record_pos=(0.401, 0.519), resolution=(1080, 2160)))
sleep(2)
t.toch_new(Template(r"tpl1581579827157.png", record_pos=(0.006, 0.263), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579858568.png", record_pos=(-0.235, -0.128), resolution=(1080, 2160)))
sleep(5)
t.toch_new(Template(r"tpl1581579877710.png", record_pos=(0.251, 0.681), resolution=(1080, 2160)))
sleep(2)
t.toch_new(Template(r"tpl1581579900061.png", record_pos=(-0.254, 0.474), resolution=(1080, 2160)))
sleep(2)
t.toch_new(Template(r"tpl1581734758843.png", record_pos=(0.007, 0.899), resolution=(1080, 2160)))


t.toch_new(Template(r"tpl1581579932854.png", record_pos=(-0.003, 0.756), resolution=(1080, 2160)))
sleep(2)
t.toch_new(Template(r"tpl1581579953652.png", record_pos=(-0.172, -0.596), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579965666.png", record_pos=(-0.001, 0.681), resolution=(1080, 2160)))
sleep(3)
t.toch_new(Template(r"tpl1581579796139.png", record_pos=(0.435, 0.917), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579796139.png", record_pos=(0.435, 0.917), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579796139.png", record_pos=(0.435, 0.917), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579796139.png", record_pos=(0.435, 0.917), resolution=(1080, 2160)))
sleep(10)
t.toch_new(Template(r"tpl1581579796139.png", record_pos=(0.435, 0.917), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579796139.png", record_pos=(0.435, 0.917), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579796139.png", record_pos=(0.435, 0.917), resolution=(1080, 2160)))
sleep(5)
t.toch_new(Template(r"tpl1581580065411.png", record_pos=(0.091, 0.246), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579796139.png", record_pos=(0.435, 0.917), resolution=(1080, 2160)))
sleep(2)
t.toch_new(Template(r"tpl1581580111323.png", record_pos=(-0.365, -0.482), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579812991.png", record_pos=(0.401, 0.519), resolution=(1080, 2160)))
sleep(2)
t.toch_new(Template(r"tpl1581580150919.png", record_pos=(-0.078, -0.808), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581580160175.png", record_pos=(0.296, -0.177), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581580168599.png", record_pos=(-0.009, 0.331), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579812991.png", record_pos=(0.401, 0.519), resolution=(1080, 2160)))
sleep(2)
t.toch_new(Template(r"tpl1581580511583.png", record_pos=(-0.149, 0.929), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581580530008.png", record_pos=(0.013, -0.39), resolution=(1080, 2160)))
sleep(3)
t.toch_new(Template(r"tpl1581735355437.png", record_pos=(0.362, -0.951), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581735355437.png", record_pos=(0.362, -0.951), resolution=(1080, 2160)))

t.toch_new(Template(r"tpl1581579812991.png", record_pos=(0.401, 0.519), resolution=(1080, 2160)))

# t.toch_new(Template(r"tpl1581580729711.png", record_pos=(-0.293, 0.923), resolution=(1080, 2160)))
# t.toch_new(Template(r"tpl1581580739578.png", record_pos=(0.123, -0.257), resolution=(1080, 2160)))
# t.toch_new(Template(r"tpl1581580746996.png", record_pos=(0.368, 0.259), resolution=(1080, 2160)))
# t.toch_new(Template(r"tpl1581580754694.png", record_pos=(0.358, 0.258), resolution=(1080, 2160)))
# t.toch_new(Template(r"tpl1581580764123.png", record_pos=(0.003, -0.048), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579812991.png", record_pos=(0.401, 0.519), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581679387429.png", record_pos=(-0.002, 0.909), resolution=(1080, 2160)))

t.toch_new(Template(r"tpl1581580796562.png", record_pos=(-0.013, 0.76), resolution=(1080, 2160)))

t.toch_new(Template(r"tpl1581580806647.png", record_pos=(0.001, -0.585), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581580815009.png", record_pos=(-0.001, 0.675), resolution=(1080, 2160)))

sleep(23)
t.toch_new(Template(r"tpl1581579812991.png", record_pos=(0.401, 0.519), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579812991.png", record_pos=(0.401, 0.519), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581580859660.png", record_pos=(-0.433, 0.918), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581580869143.png", record_pos=(0.006, 0.144), resolution=(1080, 2160)))

t.toch_new(Template(r"tpl1581580878437.png", record_pos=(-0.285, -0.053), resolution=(1080, 2160)))

t.toch_new(Template(r"tpl1581580886068.png", record_pos=(-0.028, 0.327), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579812991.png", record_pos=(0.401, 0.519), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579812991.png", record_pos=(0.401, 0.519), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581580902380.png", record_pos=(0.008, 0.27), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581580912512.png", record_pos=(-0.231, 0.527), resolution=(1080, 2160)))

sleep(5)
t.toch_new(Template(r"tpl1581580928192.png", record_pos=(0.26, 0.694), resolution=(1080, 2160)))

t.toch_new(Template(r"tpl1581580938879.png", record_pos=(-0.242, 0.475), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579812991.png", record_pos=(0.401, 0.519), resolution=(1080, 2160)))


t.toch_new(Template(r"tpl1581679387429.png", record_pos=(-0.002, 0.909), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581679696309.png", record_pos=(-0.291, 0.756), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581581386892.png", record_pos=(0.014, 0.344), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581581515294.png", record_pos=(-0.021, 0.517), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581581527462.png", record_pos=(0.447, -0.278), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581581536551.png", record_pos=(0.096, 0.232), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579812991.png", record_pos=(0.401, 0.519), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581581564795.png", record_pos=(0.004, 0.754), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581581574020.png", record_pos=(0.176, -0.581), resolution=(1080, 2160)))

t.toch_new(Template(r"tpl1581581583482.png", record_pos=(0.011, 0.685), resolution=(1080, 2160)))

sleep(20)
t.toch_new(Template(r"tpl1581579812991.png", record_pos=(0.401, 0.519), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579812991.png", record_pos=(0.401, 0.519), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581581630798.png", record_pos=(0.427, 0.924), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581581639576.png", record_pos=(-0.107, 0.363), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581581647584.png", record_pos=(0.01, 0.35), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581736821076.png", record_pos=(0.372, 0.372), resolution=(1080, 2160)))

t.toch_new(Template(r"tpl1581581663996.png", record_pos=(0.016, 0.759), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581581672720.png", record_pos=(0.004, 0.685), resolution=(1080, 2160)))

sleep(30)
t.toch_new(Template(r"tpl1581581774102.png", record_pos=(-0.049, 0.383), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581581786260.png", record_pos=(-0.014, 0.537), resolution=(1080, 2160)))

t.toch_new(Template(r"tpl1581581793863.png", record_pos=(0.078, 0.243), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579812991.png", record_pos=(0.401, 0.519), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581581808808.png", record_pos=(0.013, 0.758), resolution=(1080, 2160)))

t.toch_new(Template(r"tpl1581581818004.png", record_pos=(0.013, 0.677), resolution=(1080, 2160)))
sleep(30)
t.toch_new(Template(r"tpl1581579812991.png", record_pos=(0.401, 0.519), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579812991.png", record_pos=(0.401, 0.519), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581581869397.png", record_pos=(0.319, 0.756), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581581880032.png", record_pos=(0.332, -0.244), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581581890646.png", record_pos=(0.386, 0.26), resolution=(1080, 2160)))

t.toch_new(Template(r"tpl1581679387429.png", record_pos=(-0.002, 0.909), resolution=(1080, 2160)))
t.toch_new(Template(r"tpl1581579812991.png", record_pos=(0.401, 0.519), resolution=(1080, 2160)))

sleep(2)
t.toch_new(Template(r"../gjsg_aircase/tpl1579161442953.png", record_pos=(-0.426, 0.972), resolution=(1080, 2280)))


















# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)

