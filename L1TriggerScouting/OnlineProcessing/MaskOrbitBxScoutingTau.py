import FWCore.ParameterSet.Config as cms

def MaskOrbitBxScoutingTau(*args, **kwargs):
  mod = cms.EDProducer('MaskOrbitBxScoutingTau',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
