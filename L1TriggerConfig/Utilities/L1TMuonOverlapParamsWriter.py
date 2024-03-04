import FWCore.ParameterSet.Config as cms

def L1TMuonOverlapParamsWriter(**kwargs):
  mod = cms.EDAnalyzer('L1TMuonOverlapParamsWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
