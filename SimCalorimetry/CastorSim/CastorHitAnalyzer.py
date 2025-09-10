import FWCore.ParameterSet.Config as cms

def CastorHitAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CastorHitAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
