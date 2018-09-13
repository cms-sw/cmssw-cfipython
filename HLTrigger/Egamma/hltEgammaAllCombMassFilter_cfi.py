import FWCore.ParameterSet.Config as cms

hltEgammaAllCombMassFilter = cms.EDFilter('HLTEgammaAllCombMassFilter',
  saveTags = cms.bool(False),
  firstLegLastFilter = cms.InputTag('firstFilter'),
  secondLegLastFilter = cms.InputTag('secondFilter'),
  minMass = cms.double(-1)
)
