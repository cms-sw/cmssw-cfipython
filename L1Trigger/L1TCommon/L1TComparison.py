import FWCore.ParameterSet.Config as cms

def L1TComparison(*args, **kwargs):
  mod = cms.EDAnalyzer('L1TComparison',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
