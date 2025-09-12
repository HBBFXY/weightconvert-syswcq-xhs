weight_input=input()
kg_to_lb=2.2046
if    weight_input.endswith("kg"):
     kg = float(weight_input[:-2])
     lb = kg * kg_to_lb
     print(f"对应的英制重量为{lb:.3f}磅")
elif    weight_input.endswith("lb"):
     lb = float(weight_input[:-2])
     kg = lb / kg_to_lb
     print(f"对应的公制重量为{kg:.3f}公斤")
