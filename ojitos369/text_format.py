
class TextFormat:
    def without_acute(self, text: str) -> str:
        acutes = {
            'á': 'a',
            'é': 'e',
            'í': 'i',
            'ó': 'o',
            'ú': 'u',
            'Á': 'A',
            'É': 'E',
            'Í': 'I',
            'Ó': 'O',
            'Ú': 'U'
        }
        for acute in acutes:
            text = text.replace(acute, acutes[acute])
        return text

    def normalize_spaces(self, text: str) -> str:
        special_spaces = {
            '{ ': '{',
            ' {': '{',
            '} ': '}',
            ' }': '}',
            '[ ': '[',
            ' [': '[',
            '] ': ']',
            ' ]': ']',
            '( ': '(',
            ' (': '(',
            ') ': ')',
            ' )': ')',
        }
        if not '  ' in text:
            return text
        while True:
            text = text.replace('  ', ' ')
            if not '  ' in text:
                break
        for special_space in special_spaces:
            text = text.replace(special_space, special_spaces[special_space])
        return text

    def unique_string_no_space(self, items: list) -> str:
        if type(items) is str:
            items = items.split()
        elif type(items) is not list:
            items = [items]
        text = ''
        for item in items:
            if not item:
                continue
            item = str(item)
            item = self.without_acute(item)
            text += item.lower().replace(' ', '')
        return text

    def unique_string(self, items: str) -> str:
        text = ''
        for item in items:
            if not item:
                continue
            item = self.without_acute(item)
            item = self.normalize_spaces(item)
            text += item.lower() + ' '
        text = text[:-1]
        return text

    def normal_text(self, items: list) -> str:
        if type(items) is str:
            items = items.split()
        elif type(items) is not list:
            items = [items]
        text = ''
        for item in items:
            if not item:
                continue
            item = self.normalize_spaces(item)
            text += item + ' '
        text = text[:-1]
        text = self.normalize_spaces(text)
        return text

    def cambiar_estado(self, estado):
        ESTADOS = {
            'bajacalifornia': 'BCN',
            'bajacalifornianorte': "BCN",
            'bajacaliforniasur': "BCS",
            'aguascalientes': "AGS",
            'campeche': "CAM",
            'chihuahua': "CHI",
            'chiapas': "CHS",
            'coahuila': "COH",
            'colima': "COL",
            'distritofederal': "CDMX",
            'df': "CDMX",
            'ciudaddemexico': "CDMX",
            'cdmx': "CDMX",
            'durango': "DUR",
            'guerrero': "GRO",
            'guanajuato': "GTO",
            'hidalgo': "HGO",
            'jalisco': "JAL",
            'edo.demexico': "MEX",
            'estadodemexico': "MEX",
            'estadomexico': "MEX",
            'edomexico': "MEX",
            'mexico': "MEX",
            'michoacan': "MIC",
            'morelos': "MOR",
            'nayarit': "NAY",
            'nuevoleon': "NL",
            'oaxaca': "OAX",
            'puebla': "PUE",
            'quintanaroo': "QR",
            'queretaro': "QRO",
            'sinaloa': "SIN",
            'sanluispotosi': "SLP",
            'sonora': "SON",
            'tabasco': "TAB",
            'tamaulipas': "TAM",
            'tlaxcala': "TLX",
            'veracruz': "VER",
            'yucatan': "YUC",
            'zacatecas': "ZAC",
        }
        unique_edo = self.unique_string_no_space(estado.split())
        if unique_edo in ESTADOS:
            estado = ESTADOS[unique_edo]
        return estado
