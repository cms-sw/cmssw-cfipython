import FWCore.ParameterSet.Config as cms

def L1TMuonOverlapPhase1ParamsESProducer(*args, **kwargs):
  mod = cms.ESProducer('L1TMuonOverlapPhase1ParamsESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
