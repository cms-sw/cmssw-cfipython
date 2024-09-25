import FWCore.ParameterSet.Config as cms

def EcalGlobalShowerContainmentCorrectionsVsEtaESProducer(*args, **kwargs):
  mod = cms.ESProducer('EcalGlobalShowerContainmentCorrectionsVsEtaESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
