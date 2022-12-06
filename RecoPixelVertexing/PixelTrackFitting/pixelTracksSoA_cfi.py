import FWCore.ParameterSet.Config as cms

pixelTracksSoA = cms.EDProducer('PixelTrackSoAFromCUDA',
  src = cms.InputTag('pixelTracksCUDA'),
  mightGet = cms.optional.untracked.vstring
)
