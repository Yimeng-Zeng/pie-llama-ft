"""
A dedicated helper to manage templates and prompt building.
"""

import json
import os.path as osp
from typing import Union


class Prompter(object):
    
    __slots__ = ("template", "_verbose", "pctile_test")

    def __init__(self, template_name: str = "", verbose: bool = False):
        self._verbose = verbose
        self.pctile_test = False
        if template_name == "code_opt_w_speedup_pctile_test":
            self.pctile_test = True
            template_name = "code_opt_w_speedup_pctile"
        if not template_name:
            # Enforce the default here, so the constructor can be called with '' and will not break.
            template_name = "code_opt"
        file_name = osp.join("templates", f"{template_name}.json")
        if not osp.exists(file_name):
            raise ValueError(f"Can't read {file_name}")
        with open(file_name) as fp:
            self.template = json.load(fp)
        if self._verbose:
            print(
                f"Using prompt template {template_name}: {self.template['description']}"
            )

        print(f"template_name: {template_name}")
        print(f"pcitle_test: {self.pctile_test}")

    def generate_prompt(
        self,
        src_code: str,
        tgt_code: Union[None, str] = None,
        pctile: Union[None, str] = None,
        code_cutoff: int = 1500,
    ) -> str:
        # returns the full prompt from src_code and optional input
        # if a tgt_code (=response, =output) is provided, it's also appended.

        # cutoff both src_code and tgt_code, so the prompt is not too long
        src_code = src_code[:code_cutoff]
        
        if tgt_code:
            tgt_code = tgt_code[:code_cutoff]
            
        if pctile: 
            try: 
                res = self.template["prompt_no_input"].format(
                    src_code=src_code,
                    pctile=pctile
                )
            except Exception as e:
                print("Oops! There is no pctile in the template prompt!")
        elif self.pctile_test: # test time
            try:
                res = self.template["prompt_no_input"].format(
                    src_code=src_code,
                    pctile="10"
                )
            except Exception as e:
                print("Oops! There is no pctile in the template prompt!")
        else: # only src_code
            try:
                res = self.template["prompt_no_input"].format(
                    src_code=src_code
                )
            except Exception as e:
                print("Oops! There is no src_code in the template prompt!")
            
        if tgt_code:
            res = f"{res}{tgt_code}"
        
        if self._verbose:
            print(res)
        return res

    def get_response(self, output: str) -> str:
        return output.split(self.template["response_split"])[1].strip()
