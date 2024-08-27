import FWCore.ParameterSet.Config as cms

def EcalGlobalShowerContainmentCorrectionsVsEtaESProducer(**kwargs):
  mod = cms.ESProducer('EcalGlobalShowerContainmentCorrectionsVsEtaESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
