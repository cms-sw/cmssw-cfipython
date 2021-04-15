import FWCore.ParameterSet.Config as cms

pixelVertexSoA = cms.EDProducer('PixelVertexSoAFromCUDA',
  src = cms.InputTag('pixelVertexCUDA'),
  mightGet = cms.optional.untracked.vstring
)
