import FWCore.ParameterSet.Config as cms

def L1TMuonEndCapParamsWriter(**kwargs):
  mod = cms.EDAnalyzer('L1TMuonEndCapParamsWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
