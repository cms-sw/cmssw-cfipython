import FWCore.ParameterSet.Config as cms

def MaskOrbitBxScoutingEGamma(*args, **kwargs):
  mod = cms.EDProducer('MaskOrbitBxScoutingEGamma',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
