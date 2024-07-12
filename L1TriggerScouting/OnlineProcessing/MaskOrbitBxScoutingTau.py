import FWCore.ParameterSet.Config as cms

def MaskOrbitBxScoutingTau(**kwargs):
  mod = cms.EDProducer('MaskOrbitBxScoutingTau',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
