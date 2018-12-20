import FWCore.ParameterSet.Config as cms

hltTriMuonIsolationProducer = cms.EDProducer('HLTTriMuonIsolation',
  L3MuonsSrc = cms.InputTag('hltIterL3FromL2MuonCandidates'),
  AllMuonsSrc = cms.InputTag('hltGlbTrkMuonCands'),
  L3DiMuonsFilterSrc = cms.InputTag('hltDiMuonForTau3MuDzFiltered0p3'),
  IsoTracksSrc = cms.InputTag('hltIter2L3FromL2MuonMerged'),
  Muon1PtCut = cms.double(5),
  Muon2PtCut = cms.double(3),
  Muon3PtCut = cms.double(0),
  TriMuonPtCut = cms.double(8),
  TriMuonEtaCut = cms.double(2.5),
  ChargedAbsIsoCut = cms.double(3),
  ChargedRelIsoCut = cms.double(0.1),
  IsoConeSize = cms.double(0.5),
  MatchingConeSize = cms.double(0.03),
  MinTriMuonMass = cms.double(0.5),
  MaxTriMuonMass = cms.double(2.8),
  MaxTriMuonRadius = cms.double(0.6),
  TriMuonAbsCharge = cms.int32(-1),
  MaxDZ = cms.double(0.3),
  EnableRelIso = cms.bool(False),
  EnableAbsIso = cms.bool(True)
)
