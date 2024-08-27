import FWCore.ParameterSet.Config as cms

def dEdxHitAnalyzer(**kwargs):
  mod = cms.EDProducer('dEdxHitAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
