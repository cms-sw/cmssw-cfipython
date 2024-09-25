import FWCore.ParameterSet.Config as cms

def LHCInfoPerLSWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('LHCInfoPerLSWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
