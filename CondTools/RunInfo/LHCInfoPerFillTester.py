import FWCore.ParameterSet.Config as cms

def LHCInfoPerFillTester(*args, **kwargs):
  mod = cms.EDAnalyzer('LHCInfoPerFillTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
