import FWCore.ParameterSet.Config as cms

def SiPixelPhase1MonitorTrackSoAAlpaka(*args, **kwargs):
  mod = cms.EDProducer('SiPixelPhase1MonitorTrackSoAAlpaka',
    pixelTrackSrc = cms.InputTag('pixelTracksAlpaka'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackAlpaka'),
    useQualityCut = cms.bool(True),
    minQuality = cms.string('loose'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
