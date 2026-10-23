import FWCore.ParameterSet.Config as cms

def DTEffAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DTEffAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
