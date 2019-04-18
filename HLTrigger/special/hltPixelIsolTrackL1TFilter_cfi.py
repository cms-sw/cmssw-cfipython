import FWCore.ParameterSet.Config as cms

hltPixelIsolTrackL1TFilter = cms.EDFilter('HLTPixelIsolTrackL1TFilter',
  saveTags = cms.bool(True),
  candTag = cms.InputTag('hltIsolPixelTrackProd'),
  L1GTSeedLabel = cms.InputTag('hltL1sV0SingleJet60'),
  MaxPtNearby = cms.double(2),
  MinEnergyTrack = cms.double(2.5),
  MinPtTrack = cms.double(1.5),
  MaxEtaTrack = cms.double(1.9),
  MinEtaTrack = cms.double(0),
  MinDeltaPtL1Jet = cms.double(4),
  filterTrackEnergy = cms.bool(True),
  NMaxTrackCandidates = cms.int32(10),
  DropMultiL2Event = cms.bool(False)
)
