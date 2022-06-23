import time

# Print the top
def rectangle(global_config, rct_cfg):
    print(" "*2 + "-"*int(rct_cfg["x"]) + " "*2)

    for i in range(int(rct_cfg["y"]) - 2):
        time.sleep(float(global_config["gap"]))
        print("  |" + global_config["filling"]*(int(rct_cfg["x"])-2) + "|  ")

    time.sleep(float(global_config["gap"]))
    print(" "*2 + "-"*int(rct_cfg["x"]) + " "*2)
 