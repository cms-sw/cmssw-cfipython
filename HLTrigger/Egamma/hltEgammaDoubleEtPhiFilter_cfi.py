import FWCore.ParameterSet.Config as cms

hltEgammaDoubleEtPhiFilter = cms.EDFilter('HLTEgammaDoubleEtPhiFilter',
  saveTags = cms.bool(True),
  candTag = cms.InputTag('hltDoubleL1MatchFilter'),
  etcut1 = cms.double(6),
  etcut2 = cms.double(6),
  MinAcop = cms.double(-0.1),
  MaxAcop = cms.double(0.6),
  MinEtBalance = cms.double(-1),
  MaxEtBalance = cms.double(10),
  npaircut = cms.int32(1)
)
