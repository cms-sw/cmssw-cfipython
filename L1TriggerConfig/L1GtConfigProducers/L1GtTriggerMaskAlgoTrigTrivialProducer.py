import FWCore.ParameterSet.Config as cms

def L1GtTriggerMaskAlgoTrigTrivialProducer(*args, **kwargs):
  mod = cms.ESProducer('L1GtTriggerMaskAlgoTrigTrivialProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
