weight_input=input()
kg_to_pd=2.2046
if    weight_input.endswith("kg"):
     kg = float(weight_input[:-2])
     pd = kg * kg_to_pd
     print(f"对应的英制重量为{pd:.3f}磅")
elif    weight_input.endswith("pd"):
     pd = float(weight_input[:-2])
     kg = pd / kg_to_pd
     print(f"对应的公制重量为{kg:.3f}公斤")
