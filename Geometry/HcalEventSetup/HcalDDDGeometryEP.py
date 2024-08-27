import FWCore.ParameterSet.Config as cms

def HcalDDDGeometryEP(**kwargs):
  mod = cms.ESProducer('HcalDDDGeometryEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
