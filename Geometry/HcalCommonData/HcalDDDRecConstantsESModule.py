import FWCore.ParameterSet.Config as cms

def HcalDDDRecConstantsESModule(*args, **kwargs):
  mod = cms.ESProducer('HcalDDDRecConstantsESModule',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
