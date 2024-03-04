import FWCore.ParameterSet.Config as cms

def CastorHitAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CastorHitAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
