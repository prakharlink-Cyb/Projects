import subprocess as sb

try:
    ip = input("Enter IP: ")
    port = input("Enter port: ")

    def print_scans():
        print("\nSelect Nmap Scan Type:")
        print("1. SYN Scan (Stealth Scan)        -sS")
        print("2. TCP Connect Scan              -sT")
        print("3. UDP Scan                      -sU")
        print("4. Null Scan                     -sN")
        print("5. FIN Scan                      -sF")
        print("6. Xmas Scan                     -sX")
        print("7. ACK Scan                      -sA")
        print("8. Aggressive Scan               -A")
        print("9. Operating System Detection    -O")
        print("10. Enter custom Nmap command")

    scan_options = {
        1: "-sS",
        2: "-sT",
        3: "-sU",
        4: "-sN",
        5: "-sF",
        6: "-sX",
        7: "-sA",
        8: "-A",
        9: "-O",
    }

    print_scans()
    scan_choice = int(input("\nChoose scan number: "))

    xml_file = "scan_result.xml"
    html_file = "Final_result.html"

    if scan_choice == 10:
        custom_cmd = input(f"Enter your Nmap command (example: nmap -sS {ip} -p {port}):\n")

        command = custom_cmd.split()
        command.extend(["-oX", xml_file])

        print("\nRunning:", " ".join(command))
        sb.run(command, check=True)

    elif scan_choice in scan_options:
        scan = scan_options[scan_choice]

        command = ["nmap", scan, "-sV", "-p", port, ip, "-O", "-oX", xml_file]

        print("\nRunning:", " ".join(command))
        sb.run(command, check=True)

    else:
        print("Invalid scan choice!")
        exit()

    sb.run(["xsltproc", "-o", html_file, xml_file], check=True)

    print("\nScan completed successfully.")
    print("HTML report saved as:", html_file)

except ValueError:
    print("Please enter a valid number.")

except FileNotFoundError:
    print("Nmap or xsltproc is not installed or not in PATH.")

except sb.CalledProcessError:
    print("Error while executing Nmap command.")

except Exception as e:
    print("Unexpected error:", e)
