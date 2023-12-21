import FWCore.ParameterSet.Config as cms

ctppsInterpolatedOpticalFunctionsESSourceDefault = cms.ESProducer('CTPPSInterpolatedOpticalFunctionsESSource',
  lhcInfoLabel = cms.string(''),
  lhcInfoPerFillLabel = cms.string(''),
  lhcInfoPerLSLabel = cms.string(''),
  opticsLabel = cms.string(''),
  useNewLHCInfo = cms.bool(False),
  appendToDataLabel = cms.string('')
)
