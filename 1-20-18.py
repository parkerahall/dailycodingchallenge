def game_of_life(live, num_steps):
    assert len(live) > 0

    min_x, min_y = live[0]
    max_x, max_y = live[0]
    for live_x, live_y in live:
        min_x = min(min_x, live_x)
        max_x = max(max_x, live_x)

        min_y = min(min_y, live_y)
        max_y = max(max_y, live_y)

    live = set(live)
    for _ in range(num_steps):
        
        new_live = set()
        new_min_x = float("inf")
        new_max_x = -float("inf")
        new_min_y = float("inf")
        new_max_y = -float("inf")

        for new_y in range(min_y - 1, max_y + 2):
            
            print_list = []
            
            for new_x in range(min_x - 1, max_x + 2):
                
                num_live_neighbors = 0
                for x_delt in [-1, 0, 1]:
                    for y_delt in [-1, 0, 1]:
                        if (x_delt != 0 or y_delt != 0) and (new_x + x_delt, new_y + y_delt) in live:
                            num_live_neighbors += 1
                
                is_alive = (new_x, new_y) in live
                if new_x >= min_x and new_x <= max_x:
                    print_char = "*" if is_alive else "."
                    print_list.append(print_char)
                
                if (not is_alive and num_live_neighbors == 3) or (is_alive and (num_live_neighbors < 2 or num_live_neighbors > 3)):
                    is_alive = not is_alive

                if is_alive:
                    new_live.add((new_x, new_y))
                    new_min_x = min(new_x, new_min_x)
                    new_max_x = max(new_x, new_max_x)
                    new_min_y = min(new_y, new_min_y)
                    new_max_y = max(new_y, new_max_y)

            if new_y >= min_y and new_y <= max_y:
                print " ".join(print_list)

        if len(new_live) == 0:
            print "ALL DEAD\n"
            break
        else:
            print

        live = new_live
        min_x = new_min_x
        max_x = new_max_x
        min_y = new_min_y
        max_y = new_max_y

game_of_life([(0, 0), (1, 0), (2, 0), (2, 1), (1, 2)], 20)