import FWCore.ParameterSet.Config as cms

def Profiler(*args, **kwargs):
  mod = cms.EDAnalyzer('Profiler',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
