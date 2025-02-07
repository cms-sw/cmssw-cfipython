import FWCore.ParameterSet.Config as cms

def DDVectorRegistryESProducer(*args, **kwargs):
  mod = cms.ESProducer('DDVectorRegistryESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
