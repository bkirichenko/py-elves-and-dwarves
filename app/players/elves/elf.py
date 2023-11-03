from players.player import Player
from abc import ABC, abstractmethod


class Elf(Player, ABC):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str
    ) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass

    def play_elf_song(self) -> str:
        return f"{self.nickname} is playing a song on the " \
               f"{self._musical_instrument}"
