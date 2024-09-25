import FWCore.ParameterSet.Config as cms

def EcalTrigPrimSpikeESProducer(*args, **kwargs):
  mod = cms.ESProducer('EcalTrigPrimSpikeESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
