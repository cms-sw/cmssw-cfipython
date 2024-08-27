import FWCore.ParameterSet.Config as cms

def dEdxAnalyzer(**kwargs):
  mod = cms.EDProducer('dEdxAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
