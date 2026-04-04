import FWCore.ParameterSet.Config as cms

def GBRForestWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('GBRForestWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
