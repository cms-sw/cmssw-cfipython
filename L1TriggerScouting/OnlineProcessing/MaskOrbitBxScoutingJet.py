import FWCore.ParameterSet.Config as cms

def MaskOrbitBxScoutingJet(**kwargs):
  mod = cms.EDProducer('MaskOrbitBxScoutingJet',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
