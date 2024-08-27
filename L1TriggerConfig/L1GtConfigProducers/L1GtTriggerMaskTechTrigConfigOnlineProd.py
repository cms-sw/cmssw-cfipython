import FWCore.ParameterSet.Config as cms

def L1GtTriggerMaskTechTrigConfigOnlineProd(**kwargs):
  mod = cms.ESProducer('L1GtTriggerMaskTechTrigConfigOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
