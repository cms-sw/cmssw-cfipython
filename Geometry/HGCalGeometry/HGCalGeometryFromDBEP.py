import FWCore.ParameterSet.Config as cms

def HGCalGeometryFromDBEP(*args, **kwargs):
  mod = cms.ESProducer('HGCalGeometryFromDBEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
