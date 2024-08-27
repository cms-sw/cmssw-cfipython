import FWCore.ParameterSet.Config as cms

def L1MuonOverlapPhase1ParamsDBProducer(**kwargs):
  mod = cms.EDAnalyzer('L1MuonOverlapPhase1ParamsDBProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
