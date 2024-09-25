import FWCore.ParameterSet.Config as cms

def SiPixelHIonPhase1MonitorTrackSoA(*args, **kwargs):
  mod = cms.EDProducer('SiPixelHIonPhase1MonitorTrackSoA',
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
