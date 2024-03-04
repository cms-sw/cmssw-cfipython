import FWCore.ParameterSet.Config as cms

def EcalBasicClusterLocalContCorrectionsESProducer(**kwargs):
  mod = cms.ESProducer('EcalBasicClusterLocalContCorrectionsESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
