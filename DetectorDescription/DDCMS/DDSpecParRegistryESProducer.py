import FWCore.ParameterSet.Config as cms

def DDSpecParRegistryESProducer(**kwargs):
  mod = cms.ESProducer('DDSpecParRegistryESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
