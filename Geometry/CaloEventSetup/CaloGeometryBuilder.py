import FWCore.ParameterSet.Config as cms

def CaloGeometryBuilder(**kwargs):
  mod = cms.ESProducer('CaloGeometryBuilder',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
