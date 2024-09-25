import FWCore.ParameterSet.Config as cms

def MaskOrbitBxScoutingJet(*args, **kwargs):
  mod = cms.EDProducer('MaskOrbitBxScoutingJet',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
