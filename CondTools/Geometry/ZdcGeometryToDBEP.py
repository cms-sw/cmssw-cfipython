import FWCore.ParameterSet.Config as cms

def ZdcGeometryToDBEP(*args, **kwargs):
  mod = cms.ESProducer('ZdcGeometryToDBEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
