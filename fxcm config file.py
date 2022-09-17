import fxcm
# con = fxcmpy.fxcmpy(access_token=TOKEN, log_level='error')
con = fxcmpy.fxcmpy(config_file='fxcm.cfg')
con.is_connected()
