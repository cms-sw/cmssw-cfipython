import FWCore.ParameterSet.Config as cms

def LHCInfoPerFillWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('LHCInfoPerFillWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
