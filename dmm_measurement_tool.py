import dmm_keysight as dk
import click
from configparser import ConfigParser
import logging

@click.command()
@click.option('-m', '--measure', help='Arguments:res - 2 wire resistance; fres - 4 wire resistance; vdc - measure dc voltage; vac - measure ac voltage; idc - measure dc current; iac - measure ac current; '
                                      'av_res - avg of 10 measurements of 2 wire res;'
                                      'av_fres - avg of 10 measurements of 4 wire res;'
                                      'av_vdc - avg of 10 measurements of dc voltage;'
                                      'av_vac - avg of 10 measurements of ac voltage;'
                                      'av_idc - avg of 10 measurements of dc current;'
                                      'av_iac - avg of 10 measurements of ac current')
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

    logging.basicConfig(filename='logs/dmm_log.log', level=logging.INFO, format="%(asctime)s::%(name)s::%(levelname)s::%(message)s")

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

    if measure == "vdc":
        click.echo("Measuring dc voltage...")
        logging.info("Measuring dc voltage......")
        measured_value = dmm.measure_voltage_dc()
        click.echo(f'Measured dc voltage value is : {measured_value}')
        measured_type = 'dc voltage'

    if measure == "vac":
        click.echo("Measuring ac voltage...")
        logging.info("Measuring ac voltage......")
        measured_value = dmm.measure_voltage_ac()
        click.echo(f'Measured ac voltage value is : {measured_value}')
        measured_type = 'ac voltage'

    if measure == "idc":
        click.echo("Measuring dc current...")
        logging.info("Measuring dc current......")
        measured_value = dmm.measure_current_dc()
        click.echo(f'Measured dc current value is : {measured_value}')
        measured_type = 'dc current'

    if measure == "iac":
        click.echo("Measuring ac current...")
        logging.info("Measuring ac current......")
        measured_value = dmm.measure_current_ac()
        click.echo(f'Measured ac current value is : {measured_value}')
        measured_type = 'ac current'

    if measure == 'av_res':
        click.echo("Measuring 10 avg of 2 wire res...")
        logging.info("Measuring 10 avg of 2 wire res...")
        measured_value, std_dev = dmm.calculate_average_RES_2wire()
        click.echo(f'Calculated avg  value is : {measured_value}')
        measured_type = '2 wire avg'

    if measure == 'av_fres':
        click.echo("Measuring 10 avg of 4 wire res...")
        logging.info("Measuring 10 avg of 4 wire res...")
        measured_value, std_dev = dmm.calculate_average_RES_4wire()
        click.echo(f'Calculated avg  value is : {measured_value}')
        measured_type = '4 wire avg'

    if measure == 'av_vdc':
        click.echo("Measuring 10 avg of dc voltage...")
        logging.info("Measuring 10 avg of dc voltage...")
        measured_value, std_dev = dmm.calculate_average_voltage_DC()
        click.echo(f'Calculated avg  value is : {measured_value}')
        measured_type = 'dc voltage avg'

    if measure == 'av_vac':
        click.echo("Measuring 10 avg of ac voltage...")
        logging.info("Measuring 10 avg of ac voltage...")
        measured_value, std_dev = dmm.calculate_average_voltage_AC()
        click.echo(f'Calculated avg  value is : {measured_value}')
        measured_type = 'ac voltage avg'

    if measure == 'av_idc':
        click.echo("Measuring 10 avg of dc current...")
        logging.info("Measuring 10 avg of dc current...")
        measured_value, std_dev = dmm.calculate_average_current_dc()
        click.echo(f'Calculated avg  value is : {measured_value}')
        measured_type = 'dc current avg'

    if measure == 'av_iac':
        click.echo("Measuring 10 avg of ac current...")
        logging.info("Measuring 10 avg of ac current...")
        measured_value, std_dev = dmm.calculate_average_current_ac()
        click.echo(f'Calculated avg  value is : {measured_value}')
        measured_type = 'ac current avg'

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