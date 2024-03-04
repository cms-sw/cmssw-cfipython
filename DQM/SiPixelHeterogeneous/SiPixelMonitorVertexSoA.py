import FWCore.ParameterSet.Config as cms

def SiPixelMonitorVertexSoA(**kwargs):
  mod = cms.EDProducer('SiPixelMonitorVertexSoA',
    pixelVertexSrc = cms.InputTag('pixelVerticesSoA'),
    beamSpotSrc = cms.InputTag('offlineBeamSpot'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelVertexSoA'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
