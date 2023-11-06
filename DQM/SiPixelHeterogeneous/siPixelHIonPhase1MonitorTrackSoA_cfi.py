import FWCore.ParameterSet.Config as cms

siPixelHIonPhase1MonitorTrackSoA = cms.EDProducer('SiPixelHIonPhase1MonitorTrackSoA',
  pixelTrackSrc = cms.InputTag('pixelTracksSoA'),
  topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackSoA'),
  useQualityCut = cms.bool(True),
  minQuality = cms.string('loose'),
  mightGet = cms.optional.untracked.vstring
)
