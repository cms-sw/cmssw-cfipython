import FWCore.ParameterSet.Config as cms

def HLTCSCAcceptBusyFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTCSCAcceptBusyFilter',
    saveTags = cms.bool(True),
    cscrechitsTag = cms.InputTag('hltCsc2DRecHits'),
    invert = cms.bool(True),
    maxRecHitsPerChamber = cms.uint32(200),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
