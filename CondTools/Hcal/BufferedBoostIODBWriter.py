import FWCore.ParameterSet.Config as cms

def BufferedBoostIODBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('BufferedBoostIODBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
