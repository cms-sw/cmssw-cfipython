import FWCore.ParameterSet.Config as cms

def EcalEBTrigPrimPhase2ESProducer(**kwargs):
  mod = cms.ESProducer('EcalEBTrigPrimPhase2ESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
