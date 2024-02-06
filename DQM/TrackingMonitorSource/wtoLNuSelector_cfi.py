import FWCore.ParameterSet.Config as cms

wtoLNuSelector = cms.EDFilter('WtoLNuSelector',
  electronInputTag = cms.untracked.InputTag('gedGsfElectrons'),
  offlineBeamSpot = cms.untracked.InputTag('offlineBeamSpot'),
  muonInputTag = cms.untracked.InputTag('muons'),
  pfmetTag = cms.untracked.InputTag('pfMetT1T2Txy'),
  mightGet = cms.optional.untracked.vstring
)
