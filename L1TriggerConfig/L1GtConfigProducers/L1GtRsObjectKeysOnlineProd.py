import FWCore.ParameterSet.Config as cms

def L1GtRsObjectKeysOnlineProd(**kwargs):
  mod = cms.ESProducer('L1GtRsObjectKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
