import FWCore.ParameterSet.Config as cms

def ZdcGeometryToDBEP(**kwargs):
  mod = cms.ESProducer('ZdcGeometryToDBEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
