import FWCore.ParameterSet.Config as cms

def QualityTester(*args, **kwargs):
  mod = cms.EDProducer('QualityTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
