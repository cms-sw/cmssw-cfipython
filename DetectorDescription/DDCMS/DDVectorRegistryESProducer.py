import FWCore.ParameterSet.Config as cms

def DDVectorRegistryESProducer(**kwargs):
  mod = cms.ESProducer('DDVectorRegistryESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod