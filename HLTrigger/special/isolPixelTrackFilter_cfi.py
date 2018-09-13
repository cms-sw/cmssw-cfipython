import FWCore.ParameterSet.Config as cms

isolPixelTrackFilter = cms.EDFilter('HLTPixelIsolTrackFilter',
  saveTags = cms.bool(False),
  candTag = cms.InputTag('isolPixelTrackProd'),
  L1GTSeedLabel = cms.InputTag('hltL1sIsoTrack'),
  MaxPtNearby = cms.double(2),
  MinEnergyTrack = cms.double(15),
  MinPtTrack = cms.double(20),
  MaxEtaTrack = cms.double(1.9),
  MinEtaTrack = cms.double(0),
  MinDeltaPtL1Jet = cms.double(4),
  filterTrackEnergy = cms.bool(True),
  NMaxTrackCandidates = cms.int32(10),
  DropMultiL2Event = cms.bool(False)
)
