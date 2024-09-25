import FWCore.ParameterSet.Config as cms

def DBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('DBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
