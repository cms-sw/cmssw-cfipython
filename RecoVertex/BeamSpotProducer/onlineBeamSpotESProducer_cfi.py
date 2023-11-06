import FWCore.ParameterSet.Config as cms

onlineBeamSpotESProducer = cms.ESProducer('OnlineBeamSpotESProducer',
  timeThreshold = cms.int32(48),
  sigmaZThreshold = cms.double(2),
  sigmaXYThreshold = cms.double(4),
  appendToDataLabel = cms.string('')
)
