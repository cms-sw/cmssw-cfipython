import FWCore.ParameterSet.Config as cms

hltElectronPFMTFilterRecoElectron = cms.EDFilter('HLTGsfElectronPFMTFilter',
  saveTags = cms.bool(True),
  inputMetTag = cms.InputTag('hltPFMHT'),
  inputEleTag = cms.InputTag('hltEle25CaloIdVTTrkIdTCaloIsoTTrkIsoTTrackIsolFilter'),
  l1EGCand = cms.InputTag('hltL1IsoRecoEcalCandidate'),
  minN = cms.int32(0),
  minMht = cms.double(0),
  lowerMTCut = cms.double(0),
  upperMTCut = cms.double(9999)
)
