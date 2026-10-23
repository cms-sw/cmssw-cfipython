import FWCore.ParameterSet.Config as cms

def L1GtTriggerMaskVetoTechTrigTrivialProducer(*args, **kwargs):
  mod = cms.ESProducer('L1GtTriggerMaskVetoTechTrigTrivialProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
