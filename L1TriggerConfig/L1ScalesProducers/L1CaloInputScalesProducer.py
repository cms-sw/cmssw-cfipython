import FWCore.ParameterSet.Config as cms

def L1CaloInputScalesProducer(**kwargs):
  mod = cms.ESProducer('L1CaloInputScalesProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
