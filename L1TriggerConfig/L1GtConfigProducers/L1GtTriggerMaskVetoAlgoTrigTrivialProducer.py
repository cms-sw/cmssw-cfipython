import FWCore.ParameterSet.Config as cms

def L1GtTriggerMaskVetoAlgoTrigTrivialProducer(**kwargs):
  mod = cms.ESProducer('L1GtTriggerMaskVetoAlgoTrigTrivialProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
