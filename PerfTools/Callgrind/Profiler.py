import FWCore.ParameterSet.Config as cms

def Profiler(**kwargs):
  mod = cms.EDAnalyzer('Profiler',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
