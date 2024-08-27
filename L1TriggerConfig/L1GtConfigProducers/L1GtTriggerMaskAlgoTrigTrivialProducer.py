import FWCore.ParameterSet.Config as cms

def L1GtTriggerMaskAlgoTrigTrivialProducer(**kwargs):
  mod = cms.ESProducer('L1GtTriggerMaskAlgoTrigTrivialProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
