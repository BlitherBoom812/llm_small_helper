import time
import torch
print("hello!")
torch.zeros(1).cuda()
for i in range(120):
    time.sleep(60) # 120 min
    print(f"passed: {i} min")

print("world!")