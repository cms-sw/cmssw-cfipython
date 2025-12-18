import FWCore.ParameterSet.Config as cms

def DoodadESProducer(*args, **kwargs):
  mod = cms.ESProducer('DoodadESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
