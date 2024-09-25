import FWCore.ParameterSet.Config as cms

def PixelVertexProducerFromSoA(*args, **kwargs):
  mod = cms.EDProducer('PixelVertexProducerFromSoA',
    TrackCollection = cms.InputTag('pixelTracks'),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    src = cms.InputTag('pixelVerticesSoA'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
