import FWCore.ParameterSet.Config as cms

def DTQualPatternLutTester(**kwargs):
  mod = cms.EDAnalyzer('DTQualPatternLutTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
