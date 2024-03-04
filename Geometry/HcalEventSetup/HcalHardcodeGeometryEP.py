import FWCore.ParameterSet.Config as cms

def HcalHardcodeGeometryEP(**kwargs):
  mod = cms.ESProducer('HcalHardcodeGeometryEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
