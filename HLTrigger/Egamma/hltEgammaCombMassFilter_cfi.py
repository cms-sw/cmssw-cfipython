import FWCore.ParameterSet.Config as cms

hltEgammaCombMassFilter = cms.EDFilter('HLTEgammaCombMassFilter',
  saveTags = cms.bool(True),
  firstLegLastFilter = cms.InputTag('firstFilter'),
  secondLegLastFilter = cms.InputTag('secondFilter'),
  l1EGCand = cms.InputTag('hltEgammaCandidates'),
  minMass = cms.double(-1),
  mightGet = cms.optional.untracked.vstring
)
