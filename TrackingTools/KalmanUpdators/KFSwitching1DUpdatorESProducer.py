import FWCore.ParameterSet.Config as cms

def KFSwitching1DUpdatorESProducer(**kwargs):
  mod = cms.ESProducer('KFSwitching1DUpdatorESProducer',
    doEndCap = cms.required.bool,
    ComponentName = cms.required.string,
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
