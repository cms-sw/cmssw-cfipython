import FWCore.ParameterSet.Config as cms

def StopProfilerAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('StopProfilerAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
