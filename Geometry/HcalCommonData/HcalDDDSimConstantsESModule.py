import FWCore.ParameterSet.Config as cms

def HcalDDDSimConstantsESModule(**kwargs):
  mod = cms.ESProducer('HcalDDDSimConstantsESModule',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
