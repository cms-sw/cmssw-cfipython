import FWCore.ParameterSet.Config as cms

def ZdcHardcodeGeometryEP(*args, **kwargs):
  mod = cms.ESProducer('ZdcHardcodeGeometryEP',
    applyAlignment = cms.bool(False),
    zdcAddRPD = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
