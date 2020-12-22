from __future__ import print_function
from __future__ import division
import math
# ------------------------------------------------------------------------------------------------
# Copyright (c) 2016 Microsoft Corporation
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ------------------------------------------------------------------------------------------------

# Tutorial sample #4: Challenge - get to the centre of the sponge

from builtins import range
from past.utils import old_div
try:
    from malmo import MalmoPython
except:
    import MalmoPython
import os
import sys
import time
import json
import malmoutils
import numpy as np
if sys.version_info[0] == 2:
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately
else:
    import functools
    print = functools.partial(print, flush=True)
grid_names = []

grid_down = ""
for i in range(-10, 10):
    grid_down += '<Grid name="floorAll' + str(i) + '">'
    grid_down += '<min x="-5" y="' + str(i) + '" z="-5"/>'
    grid_down += '<max x="5" y="' + str(i) + '" z="5" />'
    grid_down += '</Grid>'
    grid_names.append('floorAll'+str(i))
    
the_grid = []

missionXML='''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
            <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            
              <About>
                <Summary>Hello world!</Summary>
              </About>
              
            <ServerSection>
              <ServerInitialConditions>
      	        <Time>
                    <StartTime>0</StartTime>
                    <AllowPassageOfTime>false</AllowPassageOfTime>
                </Time>
                <Weather>clear</Weather>
              </ServerInitialConditions>
              <ServerHandlers>
              	<FileWorldGenerator src = 'C:\\Users\\azuzo\\Desktop\\Malmo\\Minecraft\\run\\saves\\World of worlds 3.1'/>
              	<ServerQuitWhenAnyAgentFinishes/>
                </ServerHandlers>
              </ServerSection>
              
              <AgentSection mode="Creative">
                <Name>MalmoTutorialBot</Name>
                <AgentStart>
                    <Placement x="-.5" y="4" z="71.5" yaw="0" pitch="90"/>
                    <Inventory>
                        <InventoryItem slot="8" type="diamond_pickaxe"/>
                    </Inventory>
                </AgentStart>
                <AgentHandlers>
                  
                  <DiscreteMovementCommands/>
                  <ColourMapProducer>	
			      	<Width>''' + str(1024) + '''</Width>
			        <Height>''' + str(768) + '''</Height>
			      </ColourMapProducer>
                  <InventoryCommands/>
                  <VideoProducer>
                  	<Width>''' + str(1024) + '''</Width>
                    <Height>''' + str(768) + '''</Height>
                  </VideoProducer>
                  <AgentQuitFromTimeUp timeLimitMs='20000'/>
                 <ObservationFromGrid>
                      <Grid name="floorAll">
                        	<min x="-20" y="-40" z="-20"/>
                        	<max x="20" y="40" z="20"/>
                      </Grid>
                  </ObservationFromGrid>
                </AgentHandlers>
              </AgentSection>
            </Mission>'''

# Create default Malmo objects:

def load_grid(world_state):
    """
    Used the agent observation API to get a 21 X 21 grid box around the agent (the agent is in the middle).

    Args
        world_state:    <object>    current agent world state

    Returns
        grid:   <list>  the world grid blocks represented as a list of blocks (see Tutorial.pdf)
    """
    while world_state.is_mission_running:
        #sys.stdout.write(".")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        if len(world_state.errors) > 0:
            raise AssertionError('Could not load grid.')

        if world_state.number_of_observations_since_last_state > 0:
            msg = world_state.observations[-1].text
            observations = json.loads(msg)
            grid = observations.get(u'floorAll', 0)
            break
    return grid


def get_lineOfSight_observation(world_state,agent_host):
    """
    Used the agent observation API to get a 21 X 21 grid box around the agent (the agent is in the middle).

    Args
        world_state:    <object>    current agent world state

    Returns
        grid:   <list>  the world grid blocks represented as a list of blocks (see Tutorial.pdf)
    """
    ray=None
    while world_state.is_mission_running:
        #sys.stdout.write(".")
        
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        if len(world_state.errors) > 0:
            raise AssertionError('Could not load Ray.')
       
        if world_state.number_of_observations_since_last_state > 0:
	        msg = world_state.observations[-1].text
	        observations = json.loads(msg)
	      
	        ray = observations.get(u'LineOfSight')['y']
        break
   
    return ray

agent_host = MalmoPython.AgentHost()
spectator_host = MalmoPython.AgentHost()
malmoutils.parse_command_line(agent_host)
try:
    agent_host.parse( sys.argv )
except RuntimeError as e:
    print('ERROR:',e)
    print(agent_host.getUsage())
    exit(1)
if agent_host.receivedArgument("help"):
    print(agent_host.getUsage())
    exit(0)


my_mission = MalmoPython.MissionSpec(missionXML, True)
my_mission.allowAllAbsoluteMovementCommands()
my_mission.requestVideo(1024,768)
agent_recording_spec = MalmoPython.MissionRecordSpec()


# my_mission.setModeToCreative()
# my_mission.createDefaultTerrain()
recordingsDirectory = 'C:\\Users\\azuzo\\Desktop\\Malmo\\videos\\'
if recordingsDirectory:
	agent_recording_spec.setDestination(recordingsDirectory + "agent_viewpoint.tgz")
	# agent_recording_spec.recordObservations()
	print("RECORDING VIDEO:",agent_host.receivedArgument("record_video"))
	if agent_host.receivedArgument("record_video"):
		#types VIDEO,COLOUR_MAP
		
		agent_recording_spec.recordMP4(MalmoPython.FrameType.COLOUR_MAP, 1, 8000000, True)
		agent_recording_spec.recordMP4(MalmoPython.FrameType.VIDEO, 1, 8000000, True)

my_mission_record= MalmoPython.MissionRecordSpec()
# Attempt to start a mission:
max_retries = 3
for retry in range(max_retries):
    try:
        agent_host.startMission( my_mission, agent_recording_spec )
        break
    except RuntimeError as e:
        if retry == max_retries - 1:
            print("Error starting mission:",e)
            exit(1)
        else:
            time.sleep(2)

# Loop until mission starts:
print("Waiting for the mission to start ", end=' ')
world_state = agent_host.getWorldState()
height= my_mission.getVideoHeight(0)
width= my_mission.getVideoWidth(0)
print()
print('HEIGHT',height)
print('WIDTH',width)
while not world_state.has_mission_begun:
    print(".", end="")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print("Error:",error.text)

print()
print("Mission running ", end=' ')

# ADD YOUR CODE HERE
# TO GET YOUR AGENT TO THE DIAMOND BLOCK


# Loop until mission ends:

agent_host.sendCommand('setPitch 0')


past_locations=set()
agent_x=-26
agent_z=0
agent_y=71
agent_host.sendCommand('fly')
while world_state.is_mission_running:
	the_grid = []
	
	
    

	rand_x=np.random.randint(0,40)
	rand_z=np.random.randint(0,40)
	agent_x+=rand_x-20
	agent_z+=rand_z-20
	grid= np.array(load_grid(world_state))
	grid=grid.reshape(81,41,41)
	y=0
	for i in range(len(grid)-1,0,-1):
		if grid[i][rand_z][rand_x]!='air':
			delta=i
			delta=i-39
			print(delta)
			agent_y+=delta
			# print(agent_y)
			break

	# agent_host.sendCommand('tpx ' + str(agent_x+.5))
	# agent_host.sendCommand('tpz ' + str(agent_z+.5))
	# agent_host.sendCommand('tpy ' + str(agent_y))
	# time.sleep(.3)


	world_state = agent_host.getWorldState()
	for error in world_state.errors:
		print("Error:",error.text)

print()
print("Mission ended")
# Mission has ended.
