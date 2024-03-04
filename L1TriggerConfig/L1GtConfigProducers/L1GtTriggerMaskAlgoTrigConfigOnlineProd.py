import FWCore.ParameterSet.Config as cms

def L1GtTriggerMaskAlgoTrigConfigOnlineProd(**kwargs):
  mod = cms.ESProducer('L1GtTriggerMaskAlgoTrigConfigOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
