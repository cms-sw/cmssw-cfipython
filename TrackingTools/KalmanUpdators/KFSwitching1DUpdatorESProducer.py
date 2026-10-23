import FWCore.ParameterSet.Config as cms

def KFSwitching1DUpdatorESProducer(*args, **kwargs):
  mod = cms.ESProducer('KFSwitching1DUpdatorESProducer',
    doEndCap = cms.required.bool,
    ComponentName = cms.required.string,
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
