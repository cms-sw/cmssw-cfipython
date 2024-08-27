import FWCore.ParameterSet.Config as cms

def HLTHcalSimpleRecHitFilter(**kwargs):
  mod = cms.EDFilter('HLTHcalSimpleRecHitFilter',
    saveTags = cms.bool(True),
    HFRecHitCollection = cms.InputTag('hltHfreco'),
    threshold = cms.double(3),
    minNHitsNeg = cms.int32(1),
    minNHitsPos = cms.int32(1),
    doCoincidence = cms.bool(True),
    maskedChannels = cms.vuint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
