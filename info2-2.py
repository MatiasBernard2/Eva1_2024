def main():
  """
  Este script sirve para saber el ID de VLAN introducido por el usuario. Si es de rango normal,
  extendido o desconocido.
  """
  vlan_id = int(input("Introduzca el ID de VLAN: "))

  if 1 <= vlan_id <= 1005:
    print(f"La VLAN {vlan_id} es de rango normal.")
  elif 1006 <= vlan_id <= 4095:
    print(f"La VLAN {vlan_id} es de rango extendido.")
  else:
    print(f"El número de VLAN {vlan_id} es desconocido.")

if __name__ == "__main__":
  main()
