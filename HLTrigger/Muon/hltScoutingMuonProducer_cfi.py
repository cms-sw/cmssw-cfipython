import FWCore.ParameterSet.Config as cms

hltScoutingMuonProducer = cms.EDProducer('HLTScoutingMuonProducer',
  ChargedCandidates = cms.InputTag('hltIterL3MuonCandidatesNoVtx'),
  displacedvertexCollection = cms.InputTag('hltDisplacedmumuVtxProducer'),
  InputMuons = cms.InputTag('hltIterL3MuonsNoVtx'),
  InputLinks = cms.InputTag('hltL3MuonsIterL3LinksNoVtx'),
  Tracks = cms.InputTag('hltPixelTracks'),
  EcalPFClusterIsoMap = cms.InputTag('hltMuonEcalMFPFClusterIsoForMuonsNoVtx'),
  HcalPFClusterIsoMap = cms.InputTag('hltMuonHcalPFClusterIsoForMuonsNoVtx'),
  TrackIsoMap = cms.InputTag('hltMuonTkRelIsolationCut0p09MapNoVtx', 'combinedRelativeIsoDeposits'),
  muonPtCut = cms.double(3),
  muonEtaCut = cms.double(2.4),
  minVtxProbCut = cms.double(0.001),
  mightGet = cms.optional.untracked.vstring
)
