import FWCore.ParameterSet.Config as cms

def L1CaloHcalScaleConfigOnlineProd(**kwargs):
  mod = cms.ESProducer('L1CaloHcalScaleConfigOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
