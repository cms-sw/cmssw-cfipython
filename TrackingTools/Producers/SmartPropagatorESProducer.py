import FWCore.ParameterSet.Config as cms

def SmartPropagatorESProducer(*args, **kwargs):
  mod = cms.ESProducer('SmartPropagatorESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
