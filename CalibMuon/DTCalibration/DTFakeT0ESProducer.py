import FWCore.ParameterSet.Config as cms

def DTFakeT0ESProducer(*args, **kwargs):
  mod = cms.ESSource('DTFakeT0ESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
