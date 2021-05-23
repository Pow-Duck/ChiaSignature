from blspy import G1Element
from src.sized_bytes import bytes32
from src.chash import std_hash


class ProofOfSpace():
    @staticmethod
    def generate_plot_public_key(local_pk: G1Element, farmer_pk: G1Element) -> G1Element:
        return local_pk + farmer_pk

    @staticmethod
    def calculate_plot_id_pk(
        pool_public_key: G1Element,
        plot_public_key: G1Element,
    ) -> bytes32:
        return std_hash(bytes(pool_public_key) + bytes(plot_public_key))