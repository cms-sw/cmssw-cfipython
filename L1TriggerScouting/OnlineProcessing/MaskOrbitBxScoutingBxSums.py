import FWCore.ParameterSet.Config as cms

def MaskOrbitBxScoutingBxSums(*args, **kwargs):
  mod = cms.EDProducer('MaskOrbitBxScoutingBxSums',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
