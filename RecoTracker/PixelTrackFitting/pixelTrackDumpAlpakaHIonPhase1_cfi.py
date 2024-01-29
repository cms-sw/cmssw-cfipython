import FWCore.ParameterSet.Config as cms

pixelTrackDumpAlpakaHIonPhase1 = cms.EDAnalyzer('PixelTrackDumpAlpakaHIonPhase1',
  pixelTrackSrc = cms.InputTag('pixelTracksAlpaka'),
  pixelVertexSrc = cms.InputTag('pixelVerticesAlpaka'),
  mightGet = cms.optional.untracked.vstring
)
