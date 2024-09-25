import FWCore.ParameterSet.Config as cms

def HGCalGeometryToDBEP(*args, **kwargs):
  mod = cms.ESProducer('HGCalGeometryToDBEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
