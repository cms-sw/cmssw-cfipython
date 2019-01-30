import FWCore.ParameterSet.Config as cms

hltEgammaDoubleEtDeltaPhiFilter = cms.EDFilter('HLTEgammaDoubleEtDeltaPhiFilter',
  saveTags = cms.bool(False),
  inputTag = cms.InputTag('hltDoublePhotonEt5L1MatchFilterRegional'),
  L1IsoCand = cms.InputTag('hltL1IsoRecoEcalCandidate'),
  L1NonIsoCand = cms.InputTag('hltL1NonIsoRecoEcalCandidate'),
  relaxed = cms.untracked.bool(False),
  etcut = cms.double(5),
  minDeltaPhi = cms.double(2.5)
)
