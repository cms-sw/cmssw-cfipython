import FWCore.ParameterSet.Config as cms

def PixelTrackDumpAlpakaPhase2(**kwargs):
  mod = cms.EDAnalyzer('PixelTrackDumpAlpakaPhase2',
    pixelTrackSrc = cms.InputTag('pixelTracksAlpaka'),
    pixelVertexSrc = cms.InputTag('pixelVerticesAlpaka'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
