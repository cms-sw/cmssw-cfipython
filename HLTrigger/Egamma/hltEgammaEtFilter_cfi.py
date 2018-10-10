import FWCore.ParameterSet.Config as cms

hltEgammaEtFilter = cms.EDFilter('HLTEgammaEtFilter',
  saveTags = cms.bool(True),
  inputTag = cms.InputTag('HLTEgammaL1MatchFilter'),
  l1EGCand = cms.InputTag('hltL1IsoRecoEcalCandidate'),
  etcutEB = cms.double(1),
  etcutEE = cms.double(1),
  ncandcut = cms.int32(1)
)
