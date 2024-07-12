import FWCore.ParameterSet.Config as cms

def MaskOrbitBxScoutingEGamma(**kwargs):
  mod = cms.EDProducer('MaskOrbitBxScoutingEGamma',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
