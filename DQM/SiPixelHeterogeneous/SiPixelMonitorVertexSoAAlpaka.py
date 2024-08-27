import FWCore.ParameterSet.Config as cms

def SiPixelMonitorVertexSoAAlpaka(**kwargs):
  mod = cms.EDProducer('SiPixelMonitorVertexSoAAlpaka',
    pixelVertexSrc = cms.InputTag('pixelVerticesAlpaka'),
    beamSpotSrc = cms.InputTag('offlineBeamSpot'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelVertexAlpaka'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
