import FWCore.ParameterSet.Config as cms

def L1MuonOverlapParamsDBProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('L1MuonOverlapParamsDBProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
