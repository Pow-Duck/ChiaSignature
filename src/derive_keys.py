from blspy import AugSchemeMPL, PrivateKey
from typing import List


def _derive_path(sk: PrivateKey, path: List[int]) -> PrivateKey:
    for index in path:
        sk = AugSchemeMPL.derive_child_sk(sk, index)
    return sk


def master_sk_to_local_sk(master: PrivateKey) -> PrivateKey:
    return _derive_path(master, [12381, 8444, 3, 0])
