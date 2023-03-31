import FWCore.ParameterSet.Config as cms

pixelTrackSoAFromCUDAPhase1 = cms.EDProducer('PixelTrackSoAFromCUDAPhase1',
  src = cms.InputTag('pixelTracksCUDA'),
  mightGet = cms.optional.untracked.vstring
)
