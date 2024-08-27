import FWCore.ParameterSet.Config as cms

def StringResolutionProviderESProducer(**kwargs):
  mod = cms.ESProducer('StringResolutionProviderESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
