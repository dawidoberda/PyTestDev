from psu_korad.psu import PSU
import click
import logging
from configparser import ConfigParser

@click.command()
@click.option('-p', '--port', default='COM9', help="set port address for serial communication. Default is COM9")
@click.option('-v', '--voltage', default=1.0, help="set given volate on output")
@click.option('-i', '--current', default=0.5, help="set given current on output")
@click.option('-o', '--output', default='OFF', help="Set output ON or OFF")
def set(port, voltage, current, output):
    logging.basicConfig(filename="logs/korad_log.log", level=logging.INFO, format="%(asctime)s::%(name)s::%(levelname)s::%(message)s")

    psu = PSU(port)
    identificator = psu.identyfication()
    is_available = str(identificator).find("KORAD")
    if is_available == -1:
        logging.error("Korad supply unit not found")
        exit(0)
    else:
        logging.info("Korad psu status OK")

    print(is_available)
    psu.setVoltage(voltage)
    logging.info(f'Voltage is set to {voltage} V')
    psu.setCurrent(current)
    logging.info(f'Current is set to {current} A')

    if output=="OFF":
        psu.output_off()
        logging.info('Output set to OFF')
    elif output=="ON":
        psu.output_on()
        logging.info('Output set to ON')
    else:
        pass


@click.command()
@click.option('-p', '--port', default='COM9', help="set port address for serial communication. Default is COM9")
@click.option('-g', '--get', help="Return value of given param. Params: set_voltage, set_current, actual_current, actual_voltage. Example: --get actual_voltage")
def get(port, get):
    logging.basicConfig(filename="logs/korad_log.log", level=logging.INFO,
                        format="%(asctime)s::%(name)s::%(levelname)s::%(message)s")

    results = ConfigParser()

    psu = PSU(port)
    identificator = psu.identyfication()
    is_available = str(identificator).find("KORAD")
    if is_available == -1:
        logging.error("Korad supply unit not found")
        exit(0)
    else:
        logging.info("Korad psu status OK")

    output = 0

    if get == "set_voltage":
        output = psu.getSet_Voltage()
        print(f'Set voltage = {output}')
        logging.info(f'Set voltage = {output}')
        results['output'] = {
            'set_voltage': output
        }
    elif get == "set_current":
        output = psu.getSet_Current()
        print(f'Set current = {output}')
        logging.info(f'Set current = {output}')
        results['output'] = {
            'set_current': output
        }
    elif get == "actual_voltage":
        output = psu.getActual_Voltage()
        print(f'Actual voltage = {output}')
        logging.info(f'Actual voltage = {output}')
        results['output'] = {
            'actual_voltage': output
        }
    elif get == "actual_current":
        output = psu.getActual_Current()
        print(f'Actual current = {output}')
        logging.info(f'Actual current = {output}')
        results['output'] = {
            'actual_voltage': output
        }
    else:
        print("Unknown option")
        logging.error("Unknown option")

    try:
        with open('output/korad_results.ini', 'w') as f:
            results.write(f)
        logging.info('Results saved to file')
    except:
        click.echo("Unknown error during file saving")
        logging.error("Unknown error during file saving")

if __name__=="__main__":
    get()

