import FWCore.ParameterSet.Config as cms

def DTPtaLutOnlineProd(*args, **kwargs):
  mod = cms.ESProducer('DTPtaLutOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
