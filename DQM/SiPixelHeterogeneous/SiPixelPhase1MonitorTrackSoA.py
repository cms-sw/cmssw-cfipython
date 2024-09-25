import FWCore.ParameterSet.Config as cms

def SiPixelPhase1MonitorTrackSoA(*args, **kwargs):
  mod = cms.EDProducer('SiPixelPhase1MonitorTrackSoA',
    pixelTrackSrc = cms.InputTag('pixelTracksSoA'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackSoA'),
    useQualityCut = cms.bool(True),
    minQuality = cms.string('loose'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
