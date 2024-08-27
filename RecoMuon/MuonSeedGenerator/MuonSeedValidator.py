import FWCore.ParameterSet.Config as cms

def MuonSeedValidator(**kwargs):
  mod = cms.EDAnalyzer('MuonSeedValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
