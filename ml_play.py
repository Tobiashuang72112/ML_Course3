class MLPlay:
    def __init__(self, player):
        self.player = player
        if self.player == "player1":
            self.player_no = 0
        elif self.player == "player2":
            self.player_no = 1
        elif self.player == "player3":
            self.player_no = 2
        elif self.player == "player4":
            self.player_no = 3
        self.car_vel = 0                            # speed initial
        self.car_pos = (0,0)                        # pos initial
        self.car_lane = self.car_pos[0] // 70       # lanes 0 ~ 8
        self.self_car_lane = 0
        self.lanes = [35, 105, 175, 245, 315, 385, 455, 525, 595]  # lanes center
        pass

    def update(self, scene_info):
        """
        9 grid relative position
        |    |    |    |
        |  1 |  2 |  3 |
        |    |  5 |    |
        |  4 |  c |  6 |
        |    |    |    |
        |  7 |  8 |  9 |
        |    |    |    |       
        """
        for lane_center in self.lanes:
            if self.car_pos[0] == lane_center :
                self.self_car_lane = self.car_pos[0] // 70 

        def check_grid():
            grid = set()
            speed_ahead = 100
            if self.car_pos[0] <= 35: # left bound
                grid.add(1)
                grid.add(4)
                grid.add(7)
            elif self.car_pos[0] >= 595: # right bound
                grid.add(3)
                grid.add(6)
                grid.add(9)

            for car in scene_info["cars_info"]:
                if car["id"] != self.player_no:
                    x = self.car_pos[0] - car["pos"][0] # x relative position
                    y = self.car_pos[1] - car["pos"][1] # y relative position
                    carlane = car["pos"][0] // 70
                    if x <= 45 and x >= -45 :      
                        if y > 0 and y < 300:
                            grid.add(2)
                            if y < 200:
                                speed_ahead = car["velocity"]
                                grid.add(5) 
                        elif y < 0 and y > -200:
                            grid.add(8)
                    #if x > -116 and x < -40 and (self.car_lane-carlane==-1):
                    if self.self_car_lane-carlane==-1 :
                        if y > 80 and y < 200:
                            grid.add(3)
                        elif y < -80 and y > -200:
                            grid.add(9)
                        elif y < 80 and y > -80:
                            grid.add(6)
                    #if x < 116 and x > 40 and (self.car_lane-carlane==1):
                    if self.self_car_lane-carlane==1 :
                        if y > 80 and y < 200:
                            grid.add(1)
                        elif y < -80 and y > -200:
                            grid.add(7)
                        elif y < 80 and y > -80:
                            grid.add(4)
                    if self.self_car_lane==0:
                        grid.add(1)
                        grid.add(4)
                        grid.add(7)
                    if self.self_car_lane==8:
                        grid.add(3)
                        grid.add(6)
                        grid.add(9)
            return move(grid= grid, speed_ahead = speed_ahead)
            
        def move(grid, speed_ahead): 
            # if self.player_no == 0:
            #     print(grid)
            if len(grid) == 0:
                return ["SPEED"]
                
            else:
                if (5 not in grid ): # Check forward 

                    #
                    if (2 in grid ) and (self.player_no == 3) :
                        print("WHATCH OUTTTTTTT!!!")
                    if (1 not in grid) and (4 not in grid) and (2 in grid): # turn left 
                            #if  0.5 < speed_ahead - self.car_vel:
                            return ["SPEED", "MOVE_LEFT"]
                    if (3 not in grid) and (6 not in grid) and (2 in grid): # turn right 
                            #if  0.5 < speed_ahead - self.car_vel:
                            return ["SPEED", "MOVE_RIGHT"]

                    
                    #
                    # Back to lane center
                    
                    if self.car_pos[0 ] < self.lanes[self.car_lane]:
                        if self.player_no == 3:
                            print(self.self_car_lane )
                        return ["SPEED", "MOVE_RIGHT"]
                    elif self.car_pos[0] > self.lanes[self.car_lane]:
                        if self.player_no == 3:
                            print(self.self_car_lane )
                        return ["SPEED", "MOVE_LEFT"]

                    

                        
                    else :return ["SPEED"]
                else:
                    if (5 in grid): # NEED to BRAKE
                        if (4 not in grid) and (7 not in grid): # turn left 
                            if self.car_vel < speed_ahead:
                                return ["SPEED", "MOVE_LEFT"]
                            else:
                                if (self.car_pos[1]) < 720:
                                    return ["BRAKE", "MOVE_LEFT"]
                        elif (6 not in grid) and (9 not in grid): # turn right
                            if self.player_no == 3:
                                print("right ")
                            if self.car_vel < speed_ahead:
                                return ["SPEED", "MOVE_RIGHT"]
                            else:
                                if (self.car_pos[1]) < 720:
                                    return ["BRAKE", "MOVE_RIGHT"]
                        else : 
                            if self.car_vel < speed_ahead:  # BRAKE
                                return ["SPEED"]
                            else:
                                if (self.car_pos[1]) < 720:
                                    return ["BRAKE"]
                    #if (self.car_pos[0] < 60 ):
                    #    return ["SPEED", "MOVE_RIGHT"]
                    if (1 not in grid) and (4 not in grid) and (7 not in grid): # turn left 
                        if self.player_no == 3:
                            print("<----" )
                        return ["SPEED", "MOVE_LEFT"]
                    if (3 not in grid) and (6 not in grid) and (9 not in grid): # turn right
                        if self.player_no == 3:
                            print("right ")
                        return ["SPEED", "MOVE_RIGHT"]
                    if (1 not in grid) and (4 not in grid): # turn left 
                        if self.player_no == 3:
                            print("<----" )
                        return ["SPEED", "MOVE_LEFT"]
                    if (3 not in grid) and (6 not in grid): # turn right
                        if self.player_no == 3:
                            print("right ")
                        return ["SPEED", "MOVE_RIGHT"]
                    if (4 not in grid) and (7 not in grid): # turn left 
                        if self.player_no == 3:
                            print("<----" )
                        return ["MOVE_LEFT"]    
                    if (6 not in grid) and (9 not in grid): # turn right
                        if self.player_no == 3:
                            print("self.car_lane" )
                        return ["MOVE_RIGHT"]
                                
                    
        if len(scene_info[self.player]) != 0:
            self.car_pos = scene_info[self.player]

        for car in scene_info["cars_info"]:
            if car["id"]==self.player_no:
                self.car_vel = car["velocity"]

        if scene_info["status"] != "ALIVE":
            return "RESET"
        self.car_lane = self.car_pos[0] // 70
        return check_grid()

    def reset(self):
        """
        Reset the status
        """
        pass
