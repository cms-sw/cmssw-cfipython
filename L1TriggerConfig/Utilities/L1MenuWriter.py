import FWCore.ParameterSet.Config as cms

def L1MenuWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('L1MenuWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
