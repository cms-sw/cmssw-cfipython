import FWCore.ParameterSet.Config as cms

EcalLaserCorrectionService = cms.ESProducer('EcalLaserCorrectionService',
  maxExtrapolationTimeInSec = cms.uint32(0),
  appendToDataLabel = cms.string('')
)
