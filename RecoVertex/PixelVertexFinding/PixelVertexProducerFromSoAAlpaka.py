import FWCore.ParameterSet.Config as cms

def PixelVertexProducerFromSoAAlpaka(*args, **kwargs):
  mod = cms.EDProducer('PixelVertexProducerFromSoAAlpaka',
    TrackCollection = cms.InputTag('pixelTracks'),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    src = cms.InputTag('pixelVerticesAlpaka'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
