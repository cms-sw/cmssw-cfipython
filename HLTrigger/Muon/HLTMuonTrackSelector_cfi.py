import FWCore.ParameterSet.Config as cms

HLTMuonTrackSelector = cms.EDProducer('HLTMuonTrackSelector',
  track = cms.InputTag(''),
  muon = cms.InputTag(''),
  originalMVAVals = cms.InputTag(''),
  copyMVA = cms.bool(False),
  copyExtras = cms.untracked.bool(True),
  copyTrajectories = cms.untracked.bool(False)
)
