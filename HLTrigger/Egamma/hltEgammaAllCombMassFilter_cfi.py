import FWCore.ParameterSet.Config as cms

hltEgammaAllCombMassFilter = cms.EDFilter('HLTEgammaAllCombMassFilter',
  saveTags = cms.bool(True),
  firstLegLastFilter = cms.InputTag('firstFilter'),
  secondLegLastFilter = cms.InputTag('secondFilter'),
  minMass = cms.double(-1)
)
