import FWCore.ParameterSet.Config as cms

def EcalShowerContainmentCorrectionsESProducer(*args, **kwargs):
  mod = cms.ESProducer('EcalShowerContainmentCorrectionsESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
