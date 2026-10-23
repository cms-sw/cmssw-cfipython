import FWCore.ParameterSet.Config as cms

def ESTestAnalyzerL(*args, **kwargs):
  mod = cms.EDAnalyzer('ESTestAnalyzerL',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
