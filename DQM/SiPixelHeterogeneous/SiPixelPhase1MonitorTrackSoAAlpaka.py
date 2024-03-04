import FWCore.ParameterSet.Config as cms

def SiPixelPhase1MonitorTrackSoAAlpaka(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1MonitorTrackSoAAlpaka',
    pixelTrackSrc = cms.InputTag('pixelTracksAlpaka'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackAlpaka'),
    useQualityCut = cms.bool(True),
    minQuality = cms.string('loose'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
