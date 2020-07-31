import os
import subprocess

import shutil

from snake import config
from snake import error
from snake import scale


class Commands(scale.Commands):
    def check(self):
        self.capa_path = None
        if config.scale_configs['capa']['capa_path']:
            if os.path.exists(config.scale_configs['capa']['capa_path']):
                self.capa_path = config.scale_configs['capa']['capa_path']
        else:
            self.capa = shutil.which("capa")
        if not self.capa_path:
            raise error.CommandError("binary 'capa' not found")

    @scale.command({
        'info': 'This function will return the capabilities of the file passed'
    })
    def capabilities(self, args, file, opts):
        try:
            proc = subprocess.run([self.capa_path, file.file_path],
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
        except TimeoutError:
            raise error.CommandWarning("timeout when running capa")

        if proc.stderr:
            raise error.CommandWarning("an error occurred with the capa module:\n%s" % proc.stderr.decode('utf-8'))

        if proc.stdout == '':
            raise error.CommandWarning("capa returned no output")

        return {'capabilities': proc.stdout.decode('utf-8')}

    def capabilities_plaintext(self, json):
        return json['capabilities']
