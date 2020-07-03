import FWCore.ParameterSet.Config as cms

packedCandidateMuonID = cms.EDProducer('PackedCandidateMuonSelectorProducer',
  muons = cms.InputTag('muons'),
  candidates = cms.InputTag('packedPFCandidates'),
  lostTracks = cms.InputTag('lostTracks'),
  muonSelectors = cms.vstring(
    'AllTrackerMuons',
    'TMOneStationTight'
  ),
  muonIDs = cms.vstring(),
  mightGet = cms.optional.untracked.vstring
)
