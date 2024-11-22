import FWCore.ParameterSet.Config as cms

def TestGetPathStatus(*args, **kwargs):
  mod = cms.EDAnalyzer('TestGetPathStatus',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
