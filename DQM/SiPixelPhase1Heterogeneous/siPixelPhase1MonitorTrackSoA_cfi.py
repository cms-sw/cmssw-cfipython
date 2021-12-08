import FWCore.ParameterSet.Config as cms

siPixelPhase1MonitorTrackSoA = cms.EDProducer('SiPixelPhase1MonitorTrackSoA',
  pixelTrackSrc = cms.InputTag('pixelTracksSoA'),
  TopFolderName = cms.string('SiPixelHeterogeneous/PixelTrackSoA'),
  useQualityCut = cms.bool(True),
  minQuality = cms.string('loose'),
  mightGet = cms.optional.untracked.vstring
)
