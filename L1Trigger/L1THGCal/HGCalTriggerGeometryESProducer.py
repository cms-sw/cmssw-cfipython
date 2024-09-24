import FWCore.ParameterSet.Config as cms

def HGCalTriggerGeometryESProducer(*args, **kwargs):
  mod = cms.ESProducer('HGCalTriggerGeometryESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
