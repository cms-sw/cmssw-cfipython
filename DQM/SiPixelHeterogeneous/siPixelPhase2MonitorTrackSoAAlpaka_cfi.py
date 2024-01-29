import FWCore.ParameterSet.Config as cms

siPixelPhase2MonitorTrackSoAAlpaka = cms.EDProducer('SiPixelPhase2MonitorTrackSoAAlpaka',
  pixelTrackSrc = cms.InputTag('pixelTracksAlpaka'),
  topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackAlpaka'),
  useQualityCut = cms.bool(True),
  minQuality = cms.string('loose'),
  mightGet = cms.optional.untracked.vstring
)
