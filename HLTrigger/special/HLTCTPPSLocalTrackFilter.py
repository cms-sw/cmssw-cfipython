import FWCore.ParameterSet.Config as cms

def HLTCTPPSLocalTrackFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTCTPPSLocalTrackFilter',
    pixelLocalTrackInputTag = cms.InputTag('ctppsPixelLocalTracks'),
    stripLocalTrackInputTag = cms.InputTag('totemRPLocalTrackFitter'),
    diamondLocalTrackInputTag = cms.InputTag('ctppsDiamondLocalTracks'),
    usePixel = cms.bool(True),
    useStrip = cms.bool(False),
    useDiamond = cms.bool(False),
    minTracks = cms.int32(2),
    minTracksPerArm = cms.int32(1),
    maxTracks = cms.int32(-1),
    maxTracksPerArm = cms.int32(-1),
    maxTracksPerPot = cms.int32(-1),
    triggerType = cms.int32(91),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
