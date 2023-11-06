import FWCore.ParameterSet.Config as cms

pixelNtupletsFitterDefault = cms.EDProducer('PixelNtupletsFitterProducer',
  useRiemannFit = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
