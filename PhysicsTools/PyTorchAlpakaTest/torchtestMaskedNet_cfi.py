import FWCore.ParameterSet.Config as cms

from .torchtest_MaskedNet_alpaka import torchtest_MaskedNet_alpaka

torchtestMaskedNet = torchtest_MaskedNet_alpaka()
