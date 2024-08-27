import FWCore.ParameterSet.Config as cms

def L1MuonOverlapParamsDBProducer(**kwargs):
  mod = cms.EDAnalyzer('L1MuonOverlapParamsDBProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
