import FWCore.ParameterSet.Config as cms

def L1MuGMTTree(*args, **kwargs):
  mod = cms.EDAnalyzer('L1MuGMTTree',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
