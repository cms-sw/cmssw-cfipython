import FWCore.ParameterSet.Config as cms

pixelTrackDumpAlpakaPhase1 = cms.EDAnalyzer('PixelTrackDumpAlpakaPhase1',
  pixelTrackSrc = cms.InputTag('pixelTracksAlpaka'),
  pixelVertexSrc = cms.InputTag('pixelVerticesAlpaka'),
  mightGet = cms.optional.untracked.vstring
)
