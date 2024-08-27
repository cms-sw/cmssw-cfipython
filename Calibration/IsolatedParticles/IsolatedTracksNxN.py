import FWCore.ParameterSet.Config as cms

def IsolatedTracksNxN(**kwargs):
  mod = cms.EDAnalyzer('IsolatedTracksNxN',
    doMC = cms.untracked.bool(False),
    writeAllTracks = cms.untracked.bool(False),
    verbosity = cms.untracked.int32(1),
    pvTracksPtMin = cms.untracked.double(0.2),
    debugTracks = cms.untracked.int32(0),
    printTrkHitPattern = cms.untracked.bool(True),
    minTrackP = cms.untracked.double(1),
    maxTrackEta = cms.untracked.double(2.6),
    debugL1Info = cms.untracked.bool(False),
    l1TriggerAlgoInfo = cms.untracked.bool(False),
    l1extraTauJetSource = cms.InputTag('l1extraParticles', 'Tau'),
    l1extraCenJetSource = cms.InputTag('l1extraParticles', 'Central'),
    l1extraFwdJetSource = cms.InputTag('l1extraParticles', 'Forward'),
    l1extraMuonSource = cms.InputTag('l1extraParticles'),
    l1extraIsoEmSource = cms.InputTag('l1extraParticles', 'Isolated'),
    l1extraNonIsoEmSource = cms.InputTag('l1extraParticles', 'NonIsolated'),
    l1GTReadoutRcdSource = cms.InputTag('gtDigis'),
    l1GTObjectMapRcdSource = cms.InputTag('hltL1GtObjectMap'),
    jetSource = cms.InputTag('iterativeCone5CaloJets'),
    jetExtender = cms.InputTag('iterativeCone5JetExtender'),
    hbheRecHitSource = cms.InputTag('hbhereco'),
    maxNearTrackPT = cms.untracked.double(1),
    timeMinCutECAL = cms.untracked.double(-500),
    timeMaxCutECAL = cms.untracked.double(500),
    timeMinCutHCAL = cms.untracked.double(-500),
    timeMaxCutHCAL = cms.untracked.double(500),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
