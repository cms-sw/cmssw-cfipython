import FWCore.ParameterSet.Config as cms

def L1RCTSaveInput(*args, **kwargs):
  mod = cms.EDAnalyzer('L1RCTSaveInput',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
