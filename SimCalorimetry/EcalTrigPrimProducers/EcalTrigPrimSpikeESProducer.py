import FWCore.ParameterSet.Config as cms

def EcalTrigPrimSpikeESProducer(**kwargs):
  mod = cms.ESProducer('EcalTrigPrimSpikeESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
