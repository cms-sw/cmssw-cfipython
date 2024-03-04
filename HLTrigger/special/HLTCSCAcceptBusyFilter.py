import FWCore.ParameterSet.Config as cms

def HLTCSCAcceptBusyFilter(**kwargs):
  mod = cms.EDFilter('HLTCSCAcceptBusyFilter',
    saveTags = cms.bool(True),
    cscrechitsTag = cms.InputTag('hltCsc2DRecHits'),
    invert = cms.bool(True),
    maxRecHitsPerChamber = cms.uint32(200),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
