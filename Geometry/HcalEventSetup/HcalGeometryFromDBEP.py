import FWCore.ParameterSet.Config as cms

def HcalGeometryFromDBEP(**kwargs):
  mod = cms.ESProducer('HcalGeometryFromDBEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
