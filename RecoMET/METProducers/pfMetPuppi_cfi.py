import FWCore.ParameterSet.Config as cms

from .PFMETProducer import PFMETProducer

pfMetPuppi = PFMETProducer(

  applyWeight = True,
  srcWeights = ('puppiNoLep')
)
