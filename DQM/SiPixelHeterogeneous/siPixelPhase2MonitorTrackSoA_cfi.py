import FWCore.ParameterSet.Config as cms

siPixelPhase2MonitorTrackSoA = cms.EDProducer('SiPixelPhase2MonitorTrackSoA',
  pixelTrackSrc = cms.InputTag('pixelTracksSoA'),
  topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackSoA'),
  useQualityCut = cms.bool(True),
  minQuality = cms.string('loose'),
  mightGet = cms.optional.untracked.vstring
)
