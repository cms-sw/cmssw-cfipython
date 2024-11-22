import FWCore.ParameterSet.Config as cms

def SiPixelMonitorVertexSoA(*args, **kwargs):
  mod = cms.EDProducer('SiPixelMonitorVertexSoA',
    pixelVertexSrc = cms.InputTag('pixelVerticesSoA'),
    beamSpotSrc = cms.InputTag('offlineBeamSpot'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelVertexSoA'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
