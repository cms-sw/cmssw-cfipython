import FWCore.ParameterSet.Config as cms

def DBReader(*args, **kwargs):
  mod = cms.EDAnalyzer('DBReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
