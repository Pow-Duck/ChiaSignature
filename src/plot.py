from blspy import AugSchemeMPL, G1Element
from typing import Optional
from secrets import token_bytes
from src.proof_of_space import ProofOfSpace
from src.derive_keys import master_sk_to_local_sk
from src.sized_bytes import bytes32
from src.plot_tools import stream_plot_info_pk


def create_plots(public_key: str, pool_key: str) -> (str, str):
    farmer_public_key: G1Element = G1Element.from_bytes(bytes.fromhex(public_key))
    pool_public_key: Optional[G1Element] = G1Element.from_bytes(bytes.fromhex(pool_key))
    # Set random number seed
    sk = AugSchemeMPL.key_gen(token_bytes(32))
    # The plot public key is the combination of the harvester and farmer keys
    plot_public_key = ProofOfSpace.generate_plot_public_key(master_sk_to_local_sk(sk).get_g1(), farmer_public_key)

    plot_id: bytes32 = ProofOfSpace.calculate_plot_id_pk(pool_public_key, plot_public_key)
    plot_memo: bytes32 = stream_plot_info_pk(pool_public_key, farmer_public_key, sk)
    return plot_id.hex(), plot_memo.hex()
