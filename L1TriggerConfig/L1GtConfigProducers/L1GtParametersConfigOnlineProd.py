import FWCore.ParameterSet.Config as cms

def L1GtParametersConfigOnlineProd(**kwargs):
  mod = cms.ESProducer('L1GtParametersConfigOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
