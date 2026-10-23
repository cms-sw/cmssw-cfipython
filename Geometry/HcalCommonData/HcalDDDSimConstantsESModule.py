import FWCore.ParameterSet.Config as cms

def HcalDDDSimConstantsESModule(*args, **kwargs):
  mod = cms.ESProducer('HcalDDDSimConstantsESModule',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
