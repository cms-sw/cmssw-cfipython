import FWCore.ParameterSet.Config as cms

def DTQualPatternLutTester(*args, **kwargs):
  mod = cms.EDAnalyzer('DTQualPatternLutTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
