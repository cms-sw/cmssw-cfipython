import FWCore.ParameterSet.Config as cms

def SiPixelCompareVertices(*args, **kwargs):
  mod = cms.EDProducer('SiPixelCompareVertices',
    pixelVertexReferenceSoA = cms.InputTag('pixelVerticesAlpakaSerial'),
    pixelVertexTargetSoA = cms.InputTag('pixelVerticesAlpaka'),
    beamSpotSrc = cms.InputTag('offlineBeamSpot'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelVertexCompareSoADeviceVSHost'),
    dzCut = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
