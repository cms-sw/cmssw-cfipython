import FWCore.ParameterSet.Config as cms

def SiPixelPhase2CompareTracks(**kwargs):
  mod = cms.EDProducer('SiPixelPhase2CompareTracks',
    pixelTrackReferenceSoA = cms.InputTag('pixelTracksAlpakaSerial'),
    pixelTrackTargetSoA = cms.InputTag('pixelTracksAlpaka'),
    topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackCompareDeviceVSHost'),
    useQualityCut = cms.bool(True),
    minQuality = cms.string('loose'),
    deltaR2cut = cms.double(0.0004),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
