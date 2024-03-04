import FWCore.ParameterSet.Config as cms

def PixelVertexProducerFromSoA(**kwargs):
  mod = cms.EDProducer('PixelVertexProducerFromSoA',
    TrackCollection = cms.InputTag('pixelTracks'),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    src = cms.InputTag('pixelVerticesSoA'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
