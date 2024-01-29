import FWCore.ParameterSet.Config as cms

siPixelPhase1CompareTrackSoAAlpaka = cms.EDProducer('SiPixelPhase1CompareTrackSoAAlpaka',
  pixelTrackSrcHost = cms.InputTag('pixelTracksAlpakaSerial'),
  pixelTrackSrcDevice = cms.InputTag('pixelTracksAlpaka'),
  topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackCompareDeviceVSHost'),
  useQualityCut = cms.bool(True),
  minQuality = cms.string('loose'),
  deltaR2cut = cms.double(0.04),
  mightGet = cms.optional.untracked.vstring
)
