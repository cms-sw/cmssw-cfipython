import FWCore.ParameterSet.Config as cms

siPixelHIonPhase1CompareTracks = cms.EDProducer('SiPixelHIonPhase1CompareTracks',
  pixelTrackReferenceSoA = cms.InputTag('pixelTracksAlpakaSerial'),
  pixelTrackTargetSoA = cms.InputTag('pixelTracksAlpaka'),
  topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackCompareDeviceVSHost'),
  useQualityCut = cms.bool(True),
  minQuality = cms.string('loose'),
  deltaR2cut = cms.double(0.04),
  mightGet = cms.optional.untracked.vstring
)
