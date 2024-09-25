import FWCore.ParameterSet.Config as cms

def AMPTAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('AMPTAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
