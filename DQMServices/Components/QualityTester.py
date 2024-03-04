import FWCore.ParameterSet.Config as cms

def QualityTester(**kwargs):
  mod = cms.EDProducer('QualityTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
