import FWCore.ParameterSet.Config as cms

def EcalTrigPrimESProducer(*args, **kwargs):
  mod = cms.ESProducer('EcalTrigPrimESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
