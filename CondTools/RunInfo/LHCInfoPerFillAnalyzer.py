import FWCore.ParameterSet.Config as cms

def LHCInfoPerFillAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('LHCInfoPerFillAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
