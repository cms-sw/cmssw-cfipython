import FWCore.ParameterSet.Config as cms

ctppsInterpolatedOpticalFunctionsESSource = cms.ESProducer('CTPPSInterpolatedOpticalFunctionsESSource',
  lhcInfoLabel = cms.string(''),
  appendToDataLabel = cms.string('')
)
