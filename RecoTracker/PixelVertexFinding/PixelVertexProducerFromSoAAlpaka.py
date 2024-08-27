import FWCore.ParameterSet.Config as cms

def PixelVertexProducerFromSoAAlpaka(**kwargs):
  mod = cms.EDProducer('PixelVertexProducerFromSoAAlpaka',
    TrackCollection = cms.InputTag('pixelTracks'),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    src = cms.InputTag('pixelVerticesAlpaka'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
