import FWCore.ParameterSet.Config as cms

def DTConfigDBProducer(*args, **kwargs):
  mod = cms.ESProducer('DTConfigDBProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
