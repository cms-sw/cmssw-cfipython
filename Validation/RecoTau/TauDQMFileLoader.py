import FWCore.ParameterSet.Config as cms

def TauDQMFileLoader(*args, **kwargs):
  mod = cms.EDAnalyzer('TauDQMFileLoader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
