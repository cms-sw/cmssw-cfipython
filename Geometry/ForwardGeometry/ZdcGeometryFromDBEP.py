import FWCore.ParameterSet.Config as cms

def ZdcGeometryFromDBEP(**kwargs):
  mod = cms.ESProducer('ZdcGeometryFromDBEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
