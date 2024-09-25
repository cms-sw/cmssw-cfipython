import FWCore.ParameterSet.Config as cms

def DTVDriftAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DTVDriftAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
