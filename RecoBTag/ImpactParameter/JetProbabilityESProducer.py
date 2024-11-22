import FWCore.ParameterSet.Config as cms

def JetProbabilityESProducer(*args, **kwargs):
  mod = cms.ESProducer('JetProbabilityESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
