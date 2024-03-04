import FWCore.ParameterSet.Config as cms

def EgammaBasicClusters(**kwargs):
  mod = cms.EDProducer('EgammaBasicClusters',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
