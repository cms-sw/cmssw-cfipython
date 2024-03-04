import FWCore.ParameterSet.Config as cms

def CTPPSInterpolatedOpticalFunctionsESSource(**kwargs):
  mod = cms.ESProducer('CTPPSInterpolatedOpticalFunctionsESSource',
    lhcInfoLabel = cms.string(''),
    lhcInfoPerFillLabel = cms.string(''),
    lhcInfoPerLSLabel = cms.string(''),
    opticsLabel = cms.string(''),
    useNewLHCInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
