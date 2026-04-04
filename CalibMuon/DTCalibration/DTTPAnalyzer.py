import FWCore.ParameterSet.Config as cms

def DTTPAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DTTPAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
