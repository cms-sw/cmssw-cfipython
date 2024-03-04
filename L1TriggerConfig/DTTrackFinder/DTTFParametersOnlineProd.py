import FWCore.ParameterSet.Config as cms

def DTTFParametersOnlineProd(**kwargs):
  mod = cms.ESProducer('DTTFParametersOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
