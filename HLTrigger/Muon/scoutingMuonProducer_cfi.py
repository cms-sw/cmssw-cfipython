import FWCore.ParameterSet.Config as cms

scoutingMuonProducer = cms.EDProducer('HLTScoutingMuonProducer',
  ChargedCandidates = cms.InputTag('hltL3MuonCandidates'),
  Tracks = cms.InputTag('hltL3Muons'),
  EcalPFClusterIsoMap = cms.InputTag('hltMuonEcalPFClusterIsoForMuons'),
  HcalPFClusterIsoMap = cms.InputTag('hltMuonHcalPFClusterIsoForMuons'),
  TrackIsoMap = cms.InputTag('hltMuonTkRelIsolationCut0p09Map', 'combinedRelativeIsoDeposits'),
  muonPtCut = cms.double(4),
  muonEtaCut = cms.double(2.4)
)
