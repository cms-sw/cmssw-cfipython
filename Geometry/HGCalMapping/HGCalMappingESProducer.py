import FWCore.ParameterSet.Config as cms

def HGCalMappingESProducer(*args, **kwargs):
  mod = cms.ESSource('HGCalMappingESProducer',
    modules = cms.required.FileInPath,
    si = cms.required.FileInPath,
    sipm = cms.required.FileInPath,
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
