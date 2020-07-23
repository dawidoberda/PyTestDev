import dmm_keysight as dk
import click
from configparser import ConfigParser
import logging

@click.command()
@click.option('-m', '--measure', help='Arguments:res - 2 wire resistance; fres - 4 wire resistance')
@click.option('-a', '--address', default='TCPIP0::K-34461A-09586.local::hislip0::INSTR', help='Argument: Visa address of dmm. Default is TCPIP0::K-34461A-09586.local::hislip0::INSTR')
@click.option('-l', '--limits', default='0', help='Set limits for measurement [upper,lower]')
def measure(measure, address, limits):
    dmm = dk.DMM()
    judgment = ""
    measured_type = None
    measured_value = None
    lower_limit = None
    upper_limit = None
    limit_set = False

    logging.basicConfig(filename='logs/dmm_log.log', level=logging.INFO)

    connection_successful = dmm.connect(address)
    click.echo(connection_successful)
    if connection_successful:
        click.echo("Connection succesful")
        logging.info("Connection succesful")
        dmm.identificator()
    else:
        click.echo("Cannot connect to device")
        logging.error("Cannot connect to device")

    if measure == "res":
        click.echo("Measuring two wire resistance...")
        logging.info("Measuring two wire resistance...")
        measured_value = dmm.measure_resistance_2wire()
        click.echo(f'Measured resistance value is : {measured_value}')
        measured_type = '2 wire resistance'

    if measure == "fres":
        click.echo("Measuring four wire resistance...")
        logging.info("Measuring four wire resistance...")
        measured_value = dmm.measure_resistance_4wire()
        click.echo(f'Measured four wire resistance value is : {measured_value}')
        measured_type = '4 wire resistance'

    #Limits check
    if limits == "0":
        click.echo('no limits set')
        logging.info('no limits set')
        judgment = "n/a"
        lower_limit = 0
        upper_limit = 0
    else:
        try:
            lower_limit, upper_limit = str(limits).split(',')
            lower_limit = float(lower_limit)
            upper_limit = float(upper_limit)
            click.echo(f'Lower limit : {lower_limit}')
            click.echo(f'Uppper limit : {upper_limit}')
            limit_set = True
            logging.info('limits set to true')
            #Judgment
            measured_value = float(measured_value)
            if measured_value >= lower_limit and measured_value <= upper_limit:
                judgment = "Pass"
            else:
                judgment = "Fail"

            click.echo(judgment)

        except ValueError as ve:
            click.echo("Wrong input. Please try to set limits separated using comma. Example: 500,700")
            click.echo(str(ve))
            logging.error(f"Wrong input type for limit, error message : {str(ve)}")
        except:
            click.echo("Unknown error occur")
            logging.error("Unknown error occur")

    #filling results.ini
    results = ConfigParser()

    results['output'] = {
        'Measurement_type': measured_type,
        'Measurement_value': measured_value,
        'Limits_set': limit_set,
        'Lower_limit': lower_limit,
        'Upper_limit': upper_limit,
        'Judgment': judgment
    }

    try:
        with open('output/dmm_results.ini', 'w') as f:
            results.write(f)
        logging.info('Results saved to file')
    except:
        click.echo("Unknown error during file saving")
        logging.error("Unknown error during file saving")


if __name__=="__main__":
    measure()