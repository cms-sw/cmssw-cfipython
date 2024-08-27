import FWCore.ParameterSet.Config as cms

def PixelTrackDumpAlpakaHIonPhase1(**kwargs):
  mod = cms.EDAnalyzer('PixelTrackDumpAlpakaHIonPhase1',
    pixelTrackSrc = cms.InputTag('pixelTracksAlpaka'),
    pixelVertexSrc = cms.InputTag('pixelVerticesAlpaka'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
