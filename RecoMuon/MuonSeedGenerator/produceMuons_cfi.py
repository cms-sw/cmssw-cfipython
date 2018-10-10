import FWCore.ParameterSet.Config as cms

produceMuons = cms.EDProducer('MuonSeedGenerator',
  EnableDTMeasurement = cms.bool(True),
  EnableCSCMeasurement = cms.bool(True),
  EnableME0Measurement = cms.bool(False)
)
