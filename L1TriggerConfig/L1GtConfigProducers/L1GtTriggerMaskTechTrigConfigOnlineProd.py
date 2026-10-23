import FWCore.ParameterSet.Config as cms

def L1GtTriggerMaskTechTrigConfigOnlineProd(*args, **kwargs):
  mod = cms.ESProducer('L1GtTriggerMaskTechTrigConfigOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
