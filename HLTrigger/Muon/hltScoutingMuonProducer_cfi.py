import FWCore.ParameterSet.Config as cms

hltScoutingMuonProducer = cms.EDProducer('HLTScoutingMuonProducer',
  ChargedCandidates = cms.InputTag('hltL3MuonCandidates'),
  Tracks = cms.InputTag('hltL3Muons'),
  EcalPFClusterIsoMap = cms.InputTag('hltMuonEcalPFClusterIsoForMuons'),
  HcalPFClusterIsoMap = cms.InputTag('hltMuonHcalPFClusterIsoForMuons'),
  TrackIsoMap = cms.InputTag('hltMuonTkRelIsolationCut0p09Map', 'combinedRelativeIsoDeposits'),
  displacedvertexCollection = cms.InputTag('hltDisplacedmumuVtxProducerDoubleMu3NoVtx'),
  muonPtCut = cms.double(4),
  muonEtaCut = cms.double(2.4),
  minVtxProbCut = cms.double(0.001)
)
