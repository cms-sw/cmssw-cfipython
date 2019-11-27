import FWCore.ParameterSet.Config as cms

hltScoutingMuonProducer = cms.EDProducer('HLTScoutingMuonProducer',
  ChargedCandidates = cms.InputTag('hltIterL3MuonCandidates'),
  Tracks = cms.InputTag('hltPixelTracks'),
  EcalPFClusterIsoMap = cms.InputTag('hltMuonEcalMFPFClusterIsoForMuons'),
  HcalPFClusterIsoMap = cms.InputTag('hltMuonHcalRegPFClusterIsoForMuons'),
  TrackIsoMap = cms.InputTag('hltMuonTkRelIsolationCut0p07Map', 'combinedRelativeIsoDeposits'),
  displacedvertexCollection = cms.InputTag('hltPixelVertices'),
  muonPtCut = cms.double(3),
  muonEtaCut = cms.double(2.4),
  minVtxProbCut = cms.double(0.001),
  InputLinks = cms.InputTag('hltL3MuonsIterL3Links'),
  mightGet = cms.optional.untracked.vstring
)
