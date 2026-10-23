import FWCore.ParameterSet.Config as cms

def StringResolutionProviderESProducer(*args, **kwargs):
  mod = cms.ESProducer('StringResolutionProviderESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
