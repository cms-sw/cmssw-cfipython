import FWCore.ParameterSet.Config as cms

def SiPixelPhase1MonitorTrackSoA(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1MonitorTrackSoA',
    pixelTrackSrc = cms.InputTag('pixelTracksSoA'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackSoA'),
    useQualityCut = cms.bool(True),
    minQuality = cms.string('loose'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
