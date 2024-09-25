import FWCore.ParameterSet.Config as cms

def TKStatus(*args, **kwargs):
  mod = cms.EDAnalyzer('TKStatus',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
