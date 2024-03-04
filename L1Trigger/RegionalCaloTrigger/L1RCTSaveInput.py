import FWCore.ParameterSet.Config as cms

def L1RCTSaveInput(**kwargs):
  mod = cms.EDAnalyzer('L1RCTSaveInput',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
