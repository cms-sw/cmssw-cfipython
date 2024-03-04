import FWCore.ParameterSet.Config as cms

def L1HtMissScaleOnlineProd(**kwargs):
  mod = cms.ESProducer('L1HtMissScaleOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
