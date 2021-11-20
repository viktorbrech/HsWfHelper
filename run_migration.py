import config
from list_copy import copy_all_lists
from workflow_copy import copy_all_workflows
import logger
# create_input_files will create "inputs/id_mappings.json" and 'inputs/active_list_ids.json'
## comment this out for now, run create_input_files.py manually first instead
#import create_input_files

copy_all_lists(simulate=True)
#copy_all_workflows(simulate=True)
logger.write_log("simulated_list_copy_v1")
logger.write_todo("simulated_list_copy_v1")