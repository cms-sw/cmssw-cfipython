import FWCore.ParameterSet.Config as cms

hltEgammaEtFilterPairs = cms.EDFilter('HLTEgammaEtFilterPairs',
  saveTags = cms.bool(True),
  inputTag = cms.InputTag('HLTEgammaL1MatchFilter'),
  l1EGCand = cms.InputTag('hltL1IsoRecoEcalCandidate'),
  etcut1EB = cms.double(1),
  etcut1EE = cms.double(1),
  etcut2EB = cms.double(1),
  etcut2EE = cms.double(1)
)
