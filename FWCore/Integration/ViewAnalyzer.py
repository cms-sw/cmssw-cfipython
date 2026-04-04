import FWCore.ParameterSet.Config as cms

def ViewAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ViewAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
