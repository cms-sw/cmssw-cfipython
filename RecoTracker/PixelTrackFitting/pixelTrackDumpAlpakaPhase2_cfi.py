import FWCore.ParameterSet.Config as cms

pixelTrackDumpAlpakaPhase2 = cms.EDAnalyzer('PixelTrackDumpAlpakaPhase2',
  pixelTrackSrc = cms.InputTag('pixelTracksAlpaka'),
  pixelVertexSrc = cms.InputTag('pixelVerticesAlpaka'),
  mightGet = cms.optional.untracked.vstring
)
