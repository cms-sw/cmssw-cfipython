import FWCore.ParameterSet.Config as cms

pixelVerticesSoA = cms.EDProducer('PixelVertexSoAFromCUDA',
  src = cms.InputTag('pixelVerticesCUDA'),
  mightGet = cms.optional.untracked.vstring
)
