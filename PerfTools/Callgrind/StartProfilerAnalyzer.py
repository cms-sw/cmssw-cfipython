import FWCore.ParameterSet.Config as cms

def StartProfilerAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('StartProfilerAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
