import FWCore.ParameterSet.Config as cms

def DTFullMapPrint(*args, **kwargs):
  mod = cms.EDAnalyzer('DTFullMapPrint',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
