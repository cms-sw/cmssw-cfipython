import FWCore.ParameterSet.Config as cms

def SteppingHelixPropagatorESProducer(*args, **kwargs):
  mod = cms.ESProducer('SteppingHelixPropagatorESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
