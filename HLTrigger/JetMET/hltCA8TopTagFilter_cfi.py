import FWCore.ParameterSet.Config as cms

hltCA8TopTagFilter = cms.EDFilter('HLTCATopTagFilter',
  saveTags = cms.bool(True),
  TopMass = cms.double(171),
  maxTopMass = cms.double(230),
  minTopMass = cms.double(140),
  minMinMass = cms.double(50),
  src = cms.InputTag('hltParticleFlow'),
  pfsrc = cms.InputTag('selectedPFJets'),
  triggerType = cms.int32(85)
)
