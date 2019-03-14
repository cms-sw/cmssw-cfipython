import FWCore.ParameterSet.Config as cms

hltElectronMuonInvMassFilter = cms.EDFilter('HLTElectronMuonInvMassFilter',
  saveTags = cms.bool(True),
  elePrevCandTag = cms.InputTag('hltL1NonIsoHLTCaloIdTTrkIdVLSingleElectronEt8NoCandDphiFilter'),
  muonPrevCandTag = cms.InputTag('hltL1Mu0HTT50L3Filtered3'),
  lowerMassCut = cms.double(4),
  upperMassCut = cms.double(999999),
  ncandcut = cms.int32(1),
  electronRelaxed = cms.untracked.bool(True),
  ElectronL1IsoCand = cms.InputTag('hltPixelMatchElectronsActivity'),
  ElectronL1NonIsoCand = cms.InputTag('hltPixelMatchElectronsActivity'),
  MuonCand = cms.InputTag('hltL3MuonCandidates')
)
