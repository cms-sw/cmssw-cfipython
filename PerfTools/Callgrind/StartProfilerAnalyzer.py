import FWCore.ParameterSet.Config as cms

def StartProfilerAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('StartProfilerAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
