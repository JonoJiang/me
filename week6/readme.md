 the top of the screen is considered a y-coordinate of 0
 
 for k,v in human.body_parts.items():
                (POSE_COCO_BODY_PARTS[k],v.y)       #repeatedly generates a list which correspsonds a body part in dictionary with its received y coordinate
                try:                                #tests for specific k (body parts), code will only continue if these body parts are present
                    k==5
                    k==7                    
                    k==4
                    k==2
                    if k==4:                        
                        RWrist_y = v.y              #Y-coordinate of Right Wrist
                    elif k==7:                      
                        LWrist_y = v.y              #Y-coordinate of Left Wrist
                    elif k==2:                          
                        RShoulder_y = v.y           #Y-coordinate of Right Shoulder
                    elif k==5:
                        LShoulder_y = v.y           #Y-coordinate of Left Shoulder
                    elif RWrist_y < RShoulder_y:    #Tests if the right wrist is above the right shoulder
                        hail_taxi(image)
                    elif LWrist_y < LShoulder_y:    #Tests if the left wrist is above the left shoulder
                        hail_taxi(image)
                except:                             #If none of the body parts are present, don't run the if statement
                    print('No wrist or shoulder found')

Reflection:
Despite being fully functional, our method is not completely optimal. Instead of searching for specific points of the body, it searches for all relevant body parts and runs based off only 2 of them (wrist and corresponding shoulder)

It prioritises the right wrist first due to the structure of our "if" statement