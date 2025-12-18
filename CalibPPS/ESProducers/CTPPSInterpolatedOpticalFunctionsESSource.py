import FWCore.ParameterSet.Config as cms

def CTPPSInterpolatedOpticalFunctionsESSource(*args, **kwargs):
  mod = cms.ESProducer('CTPPSInterpolatedOpticalFunctionsESSource',
    lhcInfoLabel = cms.string(''),
    lhcInfoPerFillLabel = cms.string(''),
    lhcInfoPerLSLabel = cms.string(''),
    opticsLabel = cms.string(''),
    useNewLHCInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
