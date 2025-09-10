import FWCore.ParameterSet.Config as cms

def DTVDriftWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('DTVDriftWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
