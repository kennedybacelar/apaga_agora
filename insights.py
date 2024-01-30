from typing import TypedDict, Union, Any, cast




class S3Object(TypedDict):
    bucket: str
    key: str


FluidWithThicknessMap = TypedDict(
    "FluidWithThicknessMap",
    {
        "1mm": float,
        "3mm": float,
        "6mm": float,
        "thickness_map": S3Object,
    },
)

Fluid = TypedDict(
    "Fluid",
    {
        "1mm": float,
        "3mm": float,
        "6mm": float,
    },
)

# AI models versions < v1.6.0
LegacyFluid = TypedDict(
    "LegacyFluid",
    {
        "1mm": float,
        "6mm": float,
    },
)

Fluids = TypedDict(
    "Fluids",
    {
        "IRF": Union[FluidWithThicknessMap, Fluid, LegacyFluid],
        "SRF": Union[FluidWithThicknessMap, Fluid, LegacyFluid],
        "PED": Union[FluidWithThicknessMap, Fluid, LegacyFluid],
    },
)

def receive(fluids: Fluids) -> None:
    """Receive insights from the AI model."""
    pass

fluids_arg = {
    "IRF": {
        "1mm": 0.5,
        "3mm": 0.8,
        "6mm": 1.2,
        "thickness_map": {
            "bucket": "my-bucket",
            "key": "thickness_map.json"
        }
    },
    "SRF": {
        "1mm": 0.7,
        "3mm": 1.0,
        "6mm": 1.5,
        "thickness_map": {
            "bucket": "my-bucket",
            "key": "thickness_map.json"
        }
    },
    "PED": {
        "1mm": 0.9,
        "3mm": 1.3,
        "6mm": 1.8,
        "thickness_map": {
            "bucket": "my-bucket",
            "key": "thickness_map.json"
        }
    }
}

typed_fluid_data: Fluids = cast(Fluids, fluids_arg)

receive(fluids_arg) #type: ignore # TODO considering implementing generic type 
#receive(typed_fluid_data)