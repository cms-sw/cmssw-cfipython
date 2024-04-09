import FWCore.ParameterSet.Config as cms

def EcalShowerContainmentCorrectionsESProducer(**kwargs):
  mod = cms.ESProducer('EcalShowerContainmentCorrectionsESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod