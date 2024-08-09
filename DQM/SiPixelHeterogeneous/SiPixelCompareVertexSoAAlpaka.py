import FWCore.ParameterSet.Config as cms

def SiPixelCompareVertexSoAAlpaka(**kwargs):
  mod = cms.EDProducer('SiPixelCompareVertexSoAAlpaka',
    pixelVertexSrcHost = cms.InputTag('pixelVerticesAlpakaSerial'),
    pixelVertexSrcDevice = cms.InputTag('pixelVerticesAlpaka'),
    beamSpotSrc = cms.InputTag('offlineBeamSpot'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelVertexCompareSoADeviceVSHost'),
    dzCut = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
