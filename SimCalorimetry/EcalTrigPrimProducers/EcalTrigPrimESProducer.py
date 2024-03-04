import FWCore.ParameterSet.Config as cms

def EcalTrigPrimESProducer(**kwargs):
  mod = cms.ESProducer('EcalTrigPrimESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
