import FWCore.ParameterSet.Config as cms

def KFUpdatorESProducer(*args, **kwargs):
  mod = cms.ESProducer('KFUpdatorESProducer',
    ComponentName = cms.required.string,
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
