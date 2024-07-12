import FWCore.ParameterSet.Config as cms

def MaskOrbitBxScoutingBMTFStub(**kwargs):
  mod = cms.EDProducer('MaskOrbitBxScoutingBMTFStub',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
