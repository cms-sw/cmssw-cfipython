import FWCore.ParameterSet.Config as cms

def DTMapPrint(*args, **kwargs):
  mod = cms.EDAnalyzer('DTMapPrint',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
