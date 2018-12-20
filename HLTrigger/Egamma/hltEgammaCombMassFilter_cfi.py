import FWCore.ParameterSet.Config as cms

hltEgammaCombMassFilter = cms.EDFilter('HLTEgammaCombMassFilter',
  saveTags = cms.bool(True),
  firstLegLastFilter = cms.InputTag('firstFilter'),
  secondLegLastFilter = cms.InputTag('secondFilter'),
  minMass = cms.double(-1)
)
