import FWCore.ParameterSet.Config as cms

def HLTCSCActivityFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTCSCActivityFilter',
    saveTags = cms.bool(True),
    cscStripDigiTag = cms.InputTag('hltMuonCSCDigis', 'MuonCSCStripDigi'),
    skipStationRing = cms.bool(True),
    skipRingNumber = cms.int32(1),
    skipStationNumber = cms.int32(4),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
