import FWCore.ParameterSet.Config as cms

def L1MuonOverlapPhase1ParamsDBProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('L1MuonOverlapPhase1ParamsDBProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
