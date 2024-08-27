import FWCore.ParameterSet.Config as cms

def DTPtaLutOnlineProd(**kwargs):
  mod = cms.ESProducer('DTPtaLutOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
