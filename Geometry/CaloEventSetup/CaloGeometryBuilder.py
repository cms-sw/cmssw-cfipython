import FWCore.ParameterSet.Config as cms

def CaloGeometryBuilder(*args, **kwargs):
  mod = cms.ESProducer('CaloGeometryBuilder',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
