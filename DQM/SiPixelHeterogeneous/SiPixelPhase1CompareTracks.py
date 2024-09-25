import FWCore.ParameterSet.Config as cms

def SiPixelPhase1CompareTracks(*args, **kwargs):
  mod = cms.EDProducer('SiPixelPhase1CompareTracks',
    pixelTrackReferenceSoA = cms.InputTag('pixelTracksAlpakaSerial'),
    pixelTrackTargetSoA = cms.InputTag('pixelTracksAlpaka'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackCompareDeviceVSHost'),
    useQualityCut = cms.bool(True),
    minQuality = cms.string('loose'),
    deltaR2cut = cms.double(0.0004),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
