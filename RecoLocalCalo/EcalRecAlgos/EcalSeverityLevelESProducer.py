import FWCore.ParameterSet.Config as cms

def EcalSeverityLevelESProducer(**kwargs):
  mod = cms.ESProducer('EcalSeverityLevelESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
