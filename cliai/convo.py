#!/usr/bin/env python # -*- coding: utf-8 -*-

from typing import Dict, List

import openai
from cliai.util import print_not_implemented
from openai.openai_object import OpenAIObject


class MessageList(List[Dict[str, str]]):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"MessageList({super().__repr__()})"

    def __str__(self):
        return self.__repr__()

    def append(self, item: Dict[str, str]):
        if not isinstance(item, dict):
            raise TypeError("Item must be a dictionary.")
        super().append(item)

    def update_system(self, content: str):
        """
        Only the latest system prompt will be effective (experiment result).
        """
        # remove all messages with "role": "system"
        self[:] = [msg for msg in self if msg.get("role") != "system"]

        # append the new
        self.append({"role": "system", "content": content})

    def user_says(self, content: str):
        super().append({"role": "user", "content": f"{content}"})

    def assistant_says(self, content: str):
        super().append({"role": "assistant", "content": f"{content}"})

    def recall_last(self):
        super().pop()


class Presets:
    """
    The Pre-settings object.

    It includes the API settings, plus the system_role
    """
    def __init__(self, system_role):
        self.system_role: str = system_role

        self.temperature: float = temperature
        self.top_p: float = top_p

        self.max_tokens: int = max_tokens
        self.freq_penalty: float = freq_penalty
        self.pres_penalty: float = pres_penalty

        # Not sure if other settings work
        # self.nucleus_sampling = top_p
        # self.pres_penalty =
        # self.freq_penalty =
        # self.logit_bias: Dict =


class Conversation():
    """
    A conversation includes message history, some presets, and a few metadata.

    It defines what the AI character is.
    """

    def __init__(self, messages, presets, convo_title: str=None):
        if convo_name:
            self.convo_title = convo_title
        else:
            convo_title = 'Untitled'
            # TODO: If messages is not empty, ask model for the title

        # API
        self.convo_id = convo_id
        self.model = model
        self.created = created

        self.num_choices: int = 1

        self.presets = presets

        # self.user: Optional[str] = hash(user)

    def __str__(self):
        # index
        return

    def show(self):
        # only show head and the end of the conversation
        pass

    def save(self, path: str):
        """
        Export the conversation to a file.
        """
        pass

    def save_presets(self, path: str):
        pass

    def load_presets(self, path:str, overwrite: bool=True):
        pass

    # TODO
    def make_request(messages: MessageList, preset: Presets) -> OpenAIObject:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=preset.temperature,
            top_p=preset.top_p,
            max_tokens=preset.max_tokens,
        )
        return response


def make_request(messages: MessageList) -> OpenAIObject:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    return response


def save_convo(messages: MessageList) -> None:
    print_not_implemented()
    pass


def load_convo():
    # print(Fore.RED + 'This function is not available by far!')
    pass
