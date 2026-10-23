import FWCore.ParameterSet.Config as cms

def DDSpecParRegistryESProducer(*args, **kwargs):
  mod = cms.ESProducer('DDSpecParRegistryESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
