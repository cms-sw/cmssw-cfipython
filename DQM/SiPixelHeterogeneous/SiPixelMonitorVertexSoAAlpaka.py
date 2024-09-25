import FWCore.ParameterSet.Config as cms

def SiPixelMonitorVertexSoAAlpaka(*args, **kwargs):
  mod = cms.EDProducer('SiPixelMonitorVertexSoAAlpaka',
    pixelVertexSrc = cms.InputTag('pixelVerticesAlpaka'),
    beamSpotSrc = cms.InputTag('offlineBeamSpot'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelVertexAlpaka'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
