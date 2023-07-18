import FWCore.ParameterSet.Config as cms

pixelTrackSoAFromCUDAHIonPhase1 = cms.EDProducer('PixelTrackSoAFromCUDAHIonPhase1',
  src = cms.InputTag('pixelTracksCUDA'),
  mightGet = cms.optional.untracked.vstring
)
