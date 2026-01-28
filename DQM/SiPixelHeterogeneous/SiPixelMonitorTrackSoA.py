import FWCore.ParameterSet.Config as cms

def SiPixelMonitorTrackSoA(*args, **kwargs):
  mod = cms.EDProducer('SiPixelMonitorTrackSoA',
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
