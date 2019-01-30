import FWCore.ParameterSet.Config as cms

hltEgammaEtFilterPairs = cms.EDFilter('HLTEgammaEtFilterPairs',
  saveTags = cms.bool(False),
  inputTag = cms.InputTag('HLTEgammaL1MatchFilter'),
  L1IsoCand = cms.InputTag('hltL1IsoRecoEcalCandidate'),
  L1NonIsoCand = cms.InputTag('hltL1NonIsoRecoEcalCandidate'),
  relaxed = cms.untracked.bool(True),
  etcut1EB = cms.double(1),
  etcut1EE = cms.double(1),
  etcut2EB = cms.double(1),
  etcut2EE = cms.double(1)
)
