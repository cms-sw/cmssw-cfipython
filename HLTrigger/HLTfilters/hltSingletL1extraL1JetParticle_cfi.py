import FWCore.ParameterSet.Config as cms

hltSingletL1extraL1JetParticle = cms.EDFilter('HLTLevel1Jet',
  saveTags = cms.bool(True),
  inputTag = cms.InputTag('hltCollection'),
  triggerType = cms.int32(0),
  MinE = cms.double(-1),
  MinPt = cms.double(-1),
  MinMass = cms.double(-1),
  MaxEta = cms.double(-1),
  MinN = cms.int32(1)
)
