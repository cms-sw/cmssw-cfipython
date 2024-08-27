import FWCore.ParameterSet.Config as cms

def L1TMuonBarrelParamsWriter(**kwargs):
  mod = cms.EDAnalyzer('L1TMuonBarrelParamsWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
