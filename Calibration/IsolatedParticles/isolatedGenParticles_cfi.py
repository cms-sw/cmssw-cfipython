import FWCore.ParameterSet.Config as cms

isolatedGenParticles = cms.EDAnalyzer('IsolatedGenParticles',
  GenSrc = cms.untracked.string('genParticles'),
  UseHepMC = cms.untracked.bool(False),
  ChargedHadronSeedP = cms.untracked.double(1),
  PTMin = cms.untracked.double(1),
  MaxChargedHadronEta = cms.untracked.double(2.5),
  ConeRadius = cms.untracked.double(34.98),
  ConeRadiusMIP = cms.untracked.double(14),
  UseConeIsolation = cms.untracked.bool(True),
  PMaxIsolation = cms.untracked.double(5),
  Verbosity = cms.untracked.int32(0),
  DebugL1Info = cms.untracked.bool(False),
  L1extraTauJetSource = cms.untracked.InputTag('l1extraParticles', 'Tau'),
  L1extraCenJetSource = cms.untracked.InputTag('l1extraParticles', 'Central'),
  L1extraFwdJetSource = cms.untracked.InputTag('l1extraParticles', 'Forward'),
  L1extraMuonSource = cms.untracked.InputTag('l1extraParticles'),
  L1extraIsoEmSource = cms.untracked.InputTag('l1extraParticles', 'Isolated'),
  L1extraNonIsoEmSource = cms.untracked.InputTag('l1extraParticles', 'NonIsolated'),
  L1GTReadoutRcdSource = cms.untracked.InputTag('gtDigis'),
  L1GTObjectMapRcdSource = cms.untracked.InputTag('hltL1GtObjectMap'),
  mightGet = cms.optional.untracked.vstring
)
