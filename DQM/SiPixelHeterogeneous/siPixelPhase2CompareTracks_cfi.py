import FWCore.ParameterSet.Config as cms

siPixelPhase2CompareTracks = cms.EDProducer('SiPixelPhase2CompareTracks',
  pixelTrackReferenceSoA = cms.InputTag('pixelTracksAlpakaSerial'),
  pixelTrackTargetSoA = cms.InputTag('pixelTracksAlpaka'),
  topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackCompareDeviceVSHost'),
  useQualityCut = cms.bool(True),
  minQuality = cms.string('loose'),
  deltaR2cut = cms.double(0.04),
  mightGet = cms.optional.untracked.vstring
)
