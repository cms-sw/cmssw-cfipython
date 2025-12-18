import FWCore.ParameterSet.Config as cms

def dEdxHitAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('dEdxHitAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
