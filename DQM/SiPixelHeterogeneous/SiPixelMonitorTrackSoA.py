import FWCore.ParameterSet.Config as cms

def SiPixelMonitorTrackSoA(*args, **kwargs):
  mod = cms.EDProducer('SiPixelMonitorTrackSoA',
    pixelTrackSrc = cms.InputTag('pixelTracksAlpaka'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackAlpaka'),
    qualityDefinitions = cms.vstring(
      'loose',
      'highPurity'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
