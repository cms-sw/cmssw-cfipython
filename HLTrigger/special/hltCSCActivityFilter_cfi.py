import FWCore.ParameterSet.Config as cms

hltCSCActivityFilter = cms.EDFilter('HLTCSCActivityFilter',
  saveTags = cms.bool(True),
  cscStripDigiTag = cms.InputTag('hltMuonCSCDigis', 'MuonCSCStripDigi'),
  skipStationRing = cms.bool(True),
  skipRingNumber = cms.int32(1),
  skipStationNumber = cms.int32(4)
)
