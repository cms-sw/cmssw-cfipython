import FWCore.ParameterSet.Config as cms

onlineBeamSpotESProducer = cms.ESProducer('OnlineBeamSpotESProducer',
  timeThreshold = cms.int32(48),
  sigmaZThreshold = cms.double(2),
  appendToDataLabel = cms.string('')
)
