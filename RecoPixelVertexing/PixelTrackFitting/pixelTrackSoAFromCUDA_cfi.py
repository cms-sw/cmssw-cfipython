import FWCore.ParameterSet.Config as cms

pixelTrackSoAFromCUDA = cms.EDProducer('PixelTrackSoAFromCUDA',
  src = cms.InputTag('pixelTracksCUDA'),
  mightGet = cms.optional.untracked.vstring
)
