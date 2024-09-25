import FWCore.ParameterSet.Config as cms

def PixelTrackDumpAlpakaHIonPhase1(*args, **kwargs):
  mod = cms.EDAnalyzer('PixelTrackDumpAlpakaHIonPhase1',
    pixelTrackSrc = cms.InputTag('pixelTracksAlpaka'),
    pixelVertexSrc = cms.InputTag('pixelVerticesAlpaka'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
