import FWCore.ParameterSet.Config as cms

hltPixelIsolTrackFilter = cms.EDFilter('HLTPixelIsolTrackFilter',
  saveTags = cms.bool(True),
  candTag = cms.InputTag('isolPixelTrackProd'),
  L1GTSeedLabel = cms.InputTag('hltL1sIsoTrack'),
  MaxPtNearby = cms.double(2),
  MinEnergyTrack = cms.double(12),
  MinPtTrack = cms.double(3.5),
  MaxEtaTrack = cms.double(1.15),
  MinEtaTrack = cms.double(0),
  MinDeltaPtL1Jet = cms.double(-40000),
  filterTrackEnergy = cms.bool(True),
  NMaxTrackCandidates = cms.int32(10),
  DropMultiL2Event = cms.bool(False)
)
