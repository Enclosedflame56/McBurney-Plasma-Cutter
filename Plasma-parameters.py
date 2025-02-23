import curses
import sys

def material_selection(stdscr):
    # Clear screen
    stdscr.clear()
    
    # List of materials
    materials = ["Mild Steel", "Aluminum", "Stainless Steel"]

    # Dictionary of speed values based on material thickness (in inches/minute)
    speed_library = {
        "Mild Steel": [
            (0, 245),            
            (0.0179, 236.22),  
            (0.0598, 110.24),
            (0.1345, 86.61),
            (0.1875, 62.99),
            (0.25, 47.24),
            (0.33, 43.31),
            (0.4, 39.37),
            (0.5, 23.62),
            (0.625, 17.72),
            (0.75, 11.81)     
        ],
        "Aluminum": [
            (0, 275),            
            (0.0179, 271.65),  
            (0.0598, 126.77),
            (0.1345, 99.61),
            (0.1875, 72.44),
            (0.25, 54.33),
            (0.33, 49.80),
            (0.4, 45.28),
            (0.5, 27.17),
            (0.625, 20.37),
            (0.75, 13.58)     
        ],
        "Stainless Steel": [
            (0, 195),            
            (0.0179, 188.98),  
            (0.0598, 88.19),
            (0.1345, 69.29),
            (0.1875, 50.39),
            (0.25, 37.80),
            (0.33, 34.65),
            (0.4, 31.50),
            (0.5, 18.90),
            (0.625, 14.17),
            (0.75, 9.45)     
        ],
    }

    # Air Pressure library (in PSI)
    air_pressure_library = {
        "Mild Steel": [
            (0, 0),         
            (0.0179, 55),   
            (0.0598, 55),
            (0.1345, 55),
            (0.1875, 60),
            (0.25, 60),
            (0.33, 65),
            (0.4, 70),
            (0.5, 75),
            (0.625, 75),
            (0.75, 75)
        ],
        "Aluminum": [
            (0, 0),         
            (0.0179, 55),   
            (0.0598, 55),
            (0.1345, 55),
            (0.1875, 60),
            (0.25, 60),
            (0.33, 65),
            (0.4, 70),
            (0.5, 75),
            (0.625, 75),
            (0.75, 75)
        ],
        "Stainless Steel": [
            (0, 0),         
            (0.0179, 55),   
            (0.0598, 55),
            (0.1345, 55),
            (0.1875, 60),
            (0.25, 60),
            (0.33, 65),
            (0.4, 70),
            (0.5, 75),
            (0.625, 75),
            (0.75, 75)
        ],
    }

    # Current library (in Amps)
    current_library = {
        "Mild Steel": [
            (0, 0),       
            (0.0179, 20),  
            (0.0598, 30),
            (0.1345, 40),
            (0.1875, 45),
            (0.25, 45),
            (0.33, 50),
            (0.4, 55),
            (0.5, 60),
            (0.625, 60),
            (0.75, 60)
        ],
        "Aluminum": [
            (0, 0),       
            (0.0179, 20),  
            (0.0598, 30),
            (0.1345, 40),
            (0.1875, 45),
            (0.25, 45),
            (0.33, 50),
            (0.4, 55),
            (0.5, 60),
            (0.625, 60),
            (0.75, 60)
        ],
        "Stainless Steel": [
            (0, 0),       
            (0.0179, 20),  
            (0.0598, 30),
            (0.1345, 40),
            (0.1875, 45),
            (0.25, 45),
            (0.33, 50),
            (0.4, 55),
            (0.5, 60),
            (0.625, 60),
            (0.75, 60)
        ],
    }

 # Display the material options
    stdscr.addstr(0, 0, "Select your material type (enter the number corresponding to your choice and press Enter):\n")
    for idx, material in enumerate(materials):
        stdscr.addstr(idx + 1, 0, f"{idx + 1}. {material}")
    
    stdscr.refresh()
    
    # Capture user input
    while True:
        stdscr.addstr(len(materials) + 2, 0, "Enter the number of your selection: ")
        stdscr.refresh()
        
        key = stdscr.getch()
        
        # Capture the input number
        if key >= ord('1') and key <= ord('9'):  # Ensures input is a number between 1 and 9
            selected_number = key - ord('1')
            if selected_number < len(materials):
                selected_material = materials[selected_number]
                break
            else:
                stdscr.clear()
                stdscr.addstr("Invalid input. Please select a valid material number.\n")
                stdscr.refresh()


    # Clear screen and display the selected material1
    stdscr.clear()
    stdscr.addstr(f"\nYou selected: {selected_material}\n")
    
    # Ask for the material thickness
    while True:
        #stdscr.clear()  # Clear the screen to avoid overwriting
        stdscr.addstr(0, 0, "\nEnter material thickness (between 0 and 0.75 inches): \n")
        stdscr.addstr(f"\n ")
        stdscr.refresh()

        # Capture user input for thickness
        thickness = ""
        while True:
            stdscr.addstr(0, 0, "\nEnter material thickness (between 0 and 0.75 inches): \n")
            stdscr.addstr(f"{thickness}")
            stdscr.refresh()

            key = stdscr.getch()
            if key == 10:  # Enter key
                break
            elif key == 127:  # Backspace key
                thickness = thickness[:-1]
                stdscr.addstr(1, 0, f"Current input: {thickness}")  # Update the line with the current input
                stdscr.refresh()
            else:
                thickness += chr(key)
                stdscr.addstr(1, 0, f"Current input: {thickness}")  # Update the line with the current input
                stdscr.refresh()

        # Validate thickness input
        try:
            thickness_value = float(thickness)
            # Check if thickness is between 0 and 0.75
            if 0 < thickness_value <= 0.75:
                stdscr.clear()
                stdscr.addstr(f"\nYou selected a thickness of {thickness_value} inches for {selected_material}.\n")
                
                # Find the speed by interpolating (in inches/min)
                material_speeds = speed_library[selected_material]
                speed = None
                for i in range(len(material_speeds) - 1):
                    x0, y0 = material_speeds[i]
                    x1, y1 = material_speeds[i + 1]
                    if x0 <= thickness_value <= x1:
                        speed = y0 + (thickness_value - x0) * (y1 - y0) / (x1 - x0)
                        break

                # Interpolate air pressure (in PSI)
                air_pressure = None
                air_pressure_values = air_pressure_library[selected_material]
                for i in range(len(air_pressure_values) - 1):
                    x0, y0 = air_pressure_values[i]
                    x1, y1 = air_pressure_values[i + 1]
                    if x0 <= thickness_value <= x1:
                        air_pressure = y0 + (thickness_value - x0) * (y1 - y0) / (x1 - x0)
                        break

                # Interpolate current (in Volts)
                current = None
                current_values = current_library[selected_material]
                for i in range(len(current_values) - 1):
                    x0, y0 = current_values[i]
                    x1, y1 = current_values[i + 1]
                    if x0 <= thickness_value <= x1:
                        current = y0 + (thickness_value - x0) * (y1 - y0) / (x1 - x0)
                        break

                # Output the results
                if speed is not None and air_pressure is not None and current is not None:
                    stdscr.addstr(f"\nRECOMMENDED SPEED BASED ON MATERIAL SELECTION: {speed:.2f} inches/min.\n")
                    stdscr.addstr(f"    \n")
                    stdscr.addstr(f"RECOMMENDED AIR PRESSURE: {air_pressure:.2f} PSI.\n")
                    stdscr.addstr(f"    \n")
                    stdscr.addstr(f"RECOMMENDED CURRENT: {current:.2f} Amps.\n")
                else:
                    stdscr.addstr(f"\nNo parameter values found for this thickness.\n")
                
                stdscr.refresh()
                break
            else: #For input that doesn't fall within the range of the thickness capability of the plasma cutter.
                stdscr.addstr("\nPlease enter a valid thickness between 0 and 0.75 inches.\n")
                stdscr.refresh()
        except ValueError:
            stdscr.addstr("\nInvalid input. Please enter a valid number between 0 and 0.75 inches.\n")
            stdscr.refresh()

    # Wait for user to acknowledge and exit
    stdscr.getch()

    # Close the terminal
    sys.exit()

# Initialize curses
curses.wrapper(material_selection)
