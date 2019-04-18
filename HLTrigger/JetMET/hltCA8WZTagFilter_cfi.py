import FWCore.ParameterSet.Config as cms

hltCA8WZTagFilter = cms.EDFilter('HLTCAWZTagFilter',
  saveTags = cms.bool(True),
  maxWMass = cms.double(130),
  minWMass = cms.double(60),
  massdropcut = cms.double(0.4),
  src = cms.InputTag('hltParticleFlow'),
  pfsrc = cms.InputTag('selectedPFJets'),
  triggerType = cms.int32(85)
)
