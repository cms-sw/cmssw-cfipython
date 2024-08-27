import FWCore.ParameterSet.Config as cms

def HLTPPSCalFilter(**kwargs):
  mod = cms.EDFilter('HLTPPSCalFilter',
    pixelLocalTrackInputTag = cms.InputTag('ctppsPixelLocalTracks'),
    minTracks = cms.int32(1),
    maxTracks = cms.int32(-1),
    do_express = cms.bool(True),
    triggerType = cms.int32(91),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
