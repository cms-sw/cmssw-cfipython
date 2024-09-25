import FWCore.ParameterSet.Config as cms

def CPUSpender(*args, **kwargs):
  mod = cms.EDAnalyzer('CPUSpender',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
