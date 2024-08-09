import FWCore.ParameterSet.Config as cms

def SiPixelPhase2CompareTrackSoAAlpaka(**kwargs):
  mod = cms.EDProducer('SiPixelPhase2CompareTrackSoAAlpaka',
    pixelTrackSrcHost = cms.InputTag('pixelTracksAlpakaSerial'),
    pixelTrackSrcDevice = cms.InputTag('pixelTracksAlpaka'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackCompareDeviceVSHost'),
    useQualityCut = cms.bool(True),
    minQuality = cms.string('loose'),
    deltaR2cut = cms.double(0.04),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
