import math

angle_deg = float(input("Enter angle in degrees: "))
angle_rad = math.radians(angle_deg)

print("sin(", angle_deg, ") =", math.sin(angle_rad))
print("cos(", angle_deg, ") =", math.cos(angle_rad))

# Check if cosine is not zero before calculating tan
if math.cos(angle_rad) != 0:
    print("tan(", angle_deg, ") =", math.tan(angle_rad))
else:
    print("tan(", angle_deg, ") is undefined (cosine is zero)")
