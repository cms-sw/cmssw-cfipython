import FWCore.ParameterSet.Config as cms

hltPMMassFilter = cms.EDFilter('HLTPMMassFilter',
  saveTags = cms.bool(False),
  candTag = cms.InputTag('hltL1NonIsoDoublePhotonEt5UpsHcalIsolFilter'),
  beamSpot = cms.InputTag('hltOfflineBeamSpot'),
  lowerMassCut = cms.double(8),
  upperMassCut = cms.double(11),
  nZcandcut = cms.int32(1),
  reqOppCharge = cms.untracked.bool(True),
  isElectron1 = cms.untracked.bool(False),
  isElectron2 = cms.untracked.bool(False),
  relaxed = cms.untracked.bool(True),
  L1IsoCand = cms.InputTag('hltL1IsoRecoEcalCandidate'),
  L1NonIsoCand = cms.InputTag('hltL1IsoRecoEcalCandidate')
)
