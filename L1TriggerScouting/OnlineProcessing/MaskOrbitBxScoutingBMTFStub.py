import FWCore.ParameterSet.Config as cms

def MaskOrbitBxScoutingBMTFStub(*args, **kwargs):
  mod = cms.EDProducer('MaskOrbitBxScoutingBMTFStub',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
