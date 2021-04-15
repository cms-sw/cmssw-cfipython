import FWCore.ParameterSet.Config as cms

pixelTrackSoA = cms.EDProducer('PixelTrackSoAFromCUDA',
  src = cms.InputTag('caHitNtupletCUDA'),
  mightGet = cms.optional.untracked.vstring
)
