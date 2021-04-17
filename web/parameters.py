PARAMETERS = {'t': [{'name': 't вып-обр', 'optional': False, 'key': 'param1'},
                    {'name': 't обработка', 'optional': False, 'key': 'param2'},
                    {'name': 't продувка', 'optional': False, 'key': 'param4'},
                    {'name': 't под током', 'optional': False, 'key': 'param3'}],
              'ПСН': [{'name': 'ПСН гр.', 'optional': False, 'key': 'param5'}],
              'чист расход': [{'name': 'чист расход C', 'optional': False, 'key': 'param6'},
                              {'name': 'чист расход Cr', 'optional': False, 'key': 'param7'},
                              {'name': 'чист расход Mn', 'optional': False, 'key': 'param8'},
                              {'name': 'чист расход Si', 'optional': False, 'key': 'param9'},
                              {'name': 'чист расход V', 'optional': False, 'key': 'param10'}],
              'температура': [{'name': 'температура первая', 'optional': False, 'key': 'param11'},
                              {'name': 'температура последняя', 'optional': False, 'key': 'param12'}],
              'Ar': [{'name': 'Ar (интенс.)', 'optional': False, 'key': 'param13'},
                     {'name': 'расход газ Ar', 'optional': False, 'key': 'param17'}],
              'эл. энергия': [{'name': 'эл. энергия (интенс.)', 'optional': False, 'key': 'param14'},
                              {'name': 'эл. энергия', 'optional': False, 'key': 'param27'}],
              'произв': [{'name': 'произв жидкая сталь', 'optional': False, 'key': 'param15'},
                         {'name': 'произв количество обработок', 'optional': False, 'key': 'param16'}],
              'сыпуч': [{'name': 'сыпуч известь РП', 'optional': False, 'key': 'param18'},
                        {'name': 'сыпуч кокс пыль УСТК', 'optional': False, 'key': 'param19'},
                        {'name': 'сыпуч  кокс. мелочь КМ1', 'optional': False, 'key': 'param20'},
                        {'name': 'сыпуч  шпат плав.', 'optional': False, 'key': 'param21'}],
              'ферспл': [{'name': 'ферспл CaC2', 'optional': False, 'key': 'param22'},
                         {'name': 'ферспл  FeV-80', 'optional': False, 'key': 'param23'},
                         {'name': 'ферспл  Mn5Si65Al0.5', 'optional': False, 'key': 'param24'},
                         {'name': 'ферспл SiMn18', 'optional': False, 'key': 'param25'},
                         {'name': 'ферспл  фх850А', 'optional': False, 'key': 'param26'}],
              'химсталь первый': [{'name': 'химсталь первый Al_1', 'optional': False, 'key': 'param28'},
                                  {'name': 'химсталь первый C_1', 'optional': False, 'key': 'param29'},
                                  {'name': 'химсталь первый Cr_1', 'optional': False, 'key': 'param30'},
                                  {'name': 'химсталь первый Cu_1', 'optional': False, 'key': 'param31'},
                                  {'name': 'химсталь первый Mn_1', 'optional': False, 'key': 'param32'},
                                  {'name': 'химсталь первый Mo_1', 'optional': False, 'key': 'param33'},
                                  {'name': 'химсталь первый N_1', 'optional': False, 'key': 'param34'},
                                  {'name': 'химсталь первый Ni_1', 'optional': False, 'key': 'param35'},
                                  {'name': 'химсталь первый P_1', 'optional': False, 'key': 'param36'},
                                  {'name': 'химсталь первый S_1', 'optional': False, 'key': 'param37'},
                                  {'name': 'химсталь первый Si_1', 'optional': False, 'key': 'param38'},
                                  {'name': 'химсталь первый Ti_1', 'optional': False, 'key': 'param39'},
                                  {'name': 'химсталь первый V_1', 'optional': False, 'key': 'param40'}],
              'химсталь последний': [{'name': 'химсталь последний Al', 'optional': True, 'key': 'param41'},
                                     {'name': 'химсталь последний C', 'optional': False, 'key': 'param42'},
                                     {'name': 'химсталь последний Ca', 'optional': False, 'key': 'param43'},
                                     {'name': 'химсталь последний Cr', 'optional': False, 'key': 'param44'},
                                     {'name': 'химсталь последний Cu', 'optional': False, 'key': 'param45'},
                                     {'name': 'химсталь последний Mn', 'optional': False, 'key': 'param46'},
                                     {'name': 'химсталь последний Mo', 'optional': False, 'key': 'param47'},
                                     {'name': 'химсталь последний N', 'optional': False, 'key': 'param48'},
                                     {'name': 'химсталь последний Ni', 'optional': False, 'key': 'param49'},
                                     {'name': 'химсталь последний P', 'optional': False, 'key': 'param50'},
                                     {'name': 'химсталь последний S', 'optional': False, 'key': 'param51'},
                                     {'name': 'химсталь последний Si', 'optional': False, 'key': 'param52'},
                                     {'name': 'химсталь последний Ti', 'optional': False, 'key': 'param53'},
                                     {'name': 'химсталь последний V', 'optional': False, 'key': 'param54'}],
              'химшлак первый': [{'name': 'химшлак первый Al2O3_1', 'optional': False, 'key': 'param55'},
                                 {'name': 'химшлак первый CaO_1', 'optional': False, 'key': 'param56'},
                                 {'name': 'химшлак первый FeO_1', 'optional': False, 'key': 'param57'},
                                 {'name': 'химшлак первый MgO_1', 'optional': False, 'key': 'param58'},
                                 {'name': 'химшлак первый MnO_1', 'optional': False, 'key': 'param59'},
                                 {'name': 'химшлак первый R_1', 'optional': False, 'key': 'param60'},
                                 {'name': 'химшлак первый SiO2_1', 'optional': False, 'key': 'param61'}],
              'химшлак последний': [{'name': 'химшлак последний Al2O3', 'optional': False, 'key': 'param62'},
                                    {'name': 'химшлак последний CaO', 'optional': False, 'key': 'param63'},
                                    {'name': 'химшлак последний FeO', 'optional': False, 'key': 'param64'},
                                    {'name': 'химшлак последний MgO', 'optional': False, 'key': 'param65'},
                                    {'name': 'химшлак последний MnO', 'optional': False, 'key': 'param66'},
                                    {'name': 'химшлак последний R', 'optional': False, 'key': 'param67'},
                                    {'name': 'химшлак последний SiO2', 'optional': False, 'key': 'param68'}]}

KEY_TO_PARAM = {'param1': 't вып-обр', 'param2': 't обработка', 'param3': 't под током',
                'param4': 't продувка', 'param5': 'ПСН гр.', 'param6': 'чист расход C', 'param7': 'чист расход Cr',
                'param8': 'чист расход Mn', 'param9': 'чист расход Si', 'param10': 'чист расход V',
                'param11': 'температура первая', 'param12': 'температура последняя', 'param13': 'Ar (интенс.)',
                'param14': 'эл. энергия (интенс.)', 'param15': 'произв жидкая сталь',
                'param16': 'произв количество обработок', 'param17': 'расход газ Ar', 'param18': 'сыпуч известь РП',
                'param19': 'сыпуч кокс пыль УСТК', 'param20': 'сыпуч  кокс. мелочь КМ1', 'param21': 'сыпуч  шпат плав.',
                'param22': 'ферспл CaC2', 'param23': 'ферспл  FeV-80', 'param24': 'ферспл  Mn5Si65Al0.5',
                'param25': 'ферспл SiMn18', 'param26': 'ферспл  фх850А', 'param27': 'эл. энергия',
                'param28': 'химсталь первый Al_1', 'param29': 'химсталь первый C_1', 'param30': 'химсталь первый Cr_1',
                'param31': 'химсталь первый Cu_1', 'param32': 'химсталь первый Mn_1', 'param33': 'химсталь первый Mo_1',
                'param34': 'химсталь первый N_1', 'param35': 'химсталь первый Ni_1', 'param36': 'химсталь первый P_1',
                'param37': 'химсталь первый S_1', 'param38': 'химсталь первый Si_1', 'param39': 'химсталь первый Ti_1',
                'param40': 'химсталь первый V_1', 'param41': 'химсталь последний Al', 'param42': 'химсталь последний C',
                'param43': 'химсталь последний Ca', 'param44': 'химсталь последний Cr',
                'param45': 'химсталь последний Cu', 'param46': 'химсталь последний Mn',
                'param47': 'химсталь последний Mo', 'param48': 'химсталь последний N',
                'param49': 'химсталь последний Ni', 'param50': 'химсталь последний P',
                'param51': 'химсталь последний S', 'param52': 'химсталь последний Si',
                'param53': 'химсталь последний Ti', 'param54': 'химсталь последний V',
                'param55': 'химшлак первый Al2O3_1', 'param56': 'химшлак первый CaO_1',
                'param57': 'химшлак первый FeO_1', 'param58': 'химшлак первый MgO_1', 'param59': 'химшлак первый MnO_1',
                'param60': 'химшлак первый R_1', 'param61': 'химшлак первый SiO2_1',
                'param62': 'химшлак последний Al2O3', 'param63': 'химшлак последний CaO',
                'param64': 'химшлак последний FeO', 'param65': 'химшлак последний MgO',
                'param66': 'химшлак последний MnO', 'param67': 'химшлак последний R',
                'param68': 'химшлак последний SiO2'}

PARAM_TO_KEY = {v: k for k, v in KEY_TO_PARAM.items()}
