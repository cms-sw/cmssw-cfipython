import FWCore.ParameterSet.Config as cms

hltEgammaDoubleEtFilter = cms.EDFilter('HLTEgammaDoubleEtFilter',
  saveTags = cms.bool(False),
  candTag = cms.InputTag('hltTrackIsolFilter'),
  L1IsoCand = cms.InputTag('hltL1IsoRecoEcalCandidate'),
  L1NonIsoCand = cms.InputTag('hltL1NonIsoRecoEcalCandidate'),
  relaxed = cms.untracked.bool(True),
  etcut1 = cms.double(30),
  etcut2 = cms.double(20),
  npaircut = cms.int32(1)
)
