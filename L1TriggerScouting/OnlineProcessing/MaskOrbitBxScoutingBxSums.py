import FWCore.ParameterSet.Config as cms

def MaskOrbitBxScoutingBxSums(**kwargs):
  mod = cms.EDProducer('MaskOrbitBxScoutingBxSums',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
