import FWCore.ParameterSet.Config as cms

def ZdcHardcodeGeometryEP(**kwargs):
  mod = cms.ESProducer('ZdcHardcodeGeometryEP',
    applyAlignment = cms.bool(False),
    zdcAddRPD = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
