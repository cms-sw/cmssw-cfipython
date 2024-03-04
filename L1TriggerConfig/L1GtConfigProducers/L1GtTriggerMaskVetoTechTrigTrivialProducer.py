import FWCore.ParameterSet.Config as cms

def L1GtTriggerMaskVetoTechTrigTrivialProducer(**kwargs):
  mod = cms.ESProducer('L1GtTriggerMaskVetoTechTrigTrivialProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
