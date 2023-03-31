import FWCore.ParameterSet.Config as cms

pixelTrackSoAFromCUDAPhase2 = cms.EDProducer('PixelTrackSoAFromCUDAPhase2',
  src = cms.InputTag('pixelTracksCUDA'),
  mightGet = cms.optional.untracked.vstring
)
