import FWCore.ParameterSet.Config as cms

offlineToTransientBeamSpotESProducer = cms.ESProducer('OfflineToTransientBeamSpotESProducer',
  appendToDataLabel = cms.string('')
)
