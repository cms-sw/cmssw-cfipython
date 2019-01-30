import FWCore.ParameterSet.Config as cms

hltEgammaEtFilter = cms.EDFilter('HLTEgammaEtFilter',
  saveTags = cms.bool(False),
  inputTag = cms.InputTag('HLTEgammaL1MatchFilter'),
  L1IsoCand = cms.InputTag('hltL1IsoRecoEcalCandidate'),
  L1NonIsoCand = cms.InputTag('hltL1NonIsoRecoEcalCandidate'),
  relaxed = cms.untracked.bool(True),
  etcutEB = cms.double(1),
  etcutEE = cms.double(1),
  ncandcut = cms.int32(1)
)
