import click
import logging
from configparser import ConfigParser
import qrcode_tools as qr

@click.command()
@click.option('--write', '-w', default=None, help='string to be written in qr code. Param : value to decode. Example : -w 12345 . Must be use together with --file option')
@click.option('--read', '-r', default=None, help="read barcode from file. Params: file_path. Example : -r ./qr_code.png")
@click.option('--scan', '-s', default=None, help="Scan barcode and return if contains given mask. Params: mask which qrcode should consist. Example : -s word")
@click.option('--file', '-f', default=None, help='file path to save qrcode. Need to by empty while using scanning or reading option. Params: file_name . Example : -f new_qr_code.png')
def tool(write, read, scan, file):
    logging.basicConfig(filename="logs/QR_log.log", level=logging.INFO,
                        format="%(asctime)s::%(name)s::%(levelname)s::%(message)s")
    results = ConfigParser()

    #WRITER
    if write is not None:
        if read is not None:
            click.echo('Error. You cannot write and read in same time !')
            logging.error('Error. You cannot write and read in same time !')
            exit(0)
        if scan is not None:
            click.echo('Error. You cannot write and scan in same time !')
            logging.error('Error. You cannot write and scan in same time !')
            exit(0)
        if file is None:
            click.echo('Error. You need to specify path !')
            logging.error('Error. You need to specify path !')
            exit(0)

        writter = qr.QR_Writer()
        try:
            writter.generate(write)
            logging.info('QR code generation success.')
            writter.save(file, scale=8)
        except :
            click.echo('Something went wrong during generating qr code ')
            logging.error('Something went wrong during generating qr code ')

    #READER
    if read is not None:
        if write is not None:
            click.echo('Error. You cannot write and read in same time !')
            logging.error('Error. You cannot write and read in same time !')
            exit(0)
        if scan is not None:
            click.echo('Error. You cannot write and scan in same time !')
            logging.error('Error. You cannot write and scan in same time !')
            exit(0)
        if file is not None:
            click.echo('Error. You cannot use this option here !!')
            logging.error('Error. You cannot use this option here !!')
            exit(0)
        reader = qr.QR_Reader()
        try:
            decoded_text = reader.read(read)
            click.echo(decoded_text)
            logging.info(f'Value decoded from qr code : {decoded_text}')
            results['output'] = {
                'decoded value': decoded_text
            }
        except :
            click.echo("Something went wrong during reading barcode")
            logging.error("Something went wrong during reading barcode")


    #SCANNER
    if scan is not None:
        if write is not None:
            click.echo('Error. You cannot write and scan in same time !')
            logging.error('Error. You cannot write and scan in same time !')
            exit(0)
        if read is not None:
            click.echo('Error. You cannot read and scan in same time !')
            logging.error('Error. You cannot read and scan in same time !')
            exit(0)
        if file is not None:
            click.echo('Error. You cannot use this option here !!')
            logging.error('Error. You cannot use this option here !!')
            exit(0)

        scanner = qr.QR_scanner()
        scanned_value = scanner.scan(scan)
        click.echo(scanned_value)
        logging.info(f'Scanned value is = {scanned_value}')
        results['output'] = {
            'scanned value': scanned_value
        }

    try:
        with open('output/QR_results.ini', 'w') as f:
            results.write(f)
        logging.info('Results saved to file')
    except:
        click.echo("Unknown error during file saving")
        logging.error("Unknown error during file saving")

if __name__ == "__main__":
    tool()