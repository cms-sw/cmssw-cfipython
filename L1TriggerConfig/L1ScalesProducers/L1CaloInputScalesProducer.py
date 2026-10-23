import FWCore.ParameterSet.Config as cms

def L1CaloInputScalesProducer(*args, **kwargs):
  mod = cms.ESProducer('L1CaloInputScalesProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
