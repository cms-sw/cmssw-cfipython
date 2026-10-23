import FWCore.ParameterSet.Config as cms

def DTEtaPatternLutTester(*args, **kwargs):
  mod = cms.EDAnalyzer('DTEtaPatternLutTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
