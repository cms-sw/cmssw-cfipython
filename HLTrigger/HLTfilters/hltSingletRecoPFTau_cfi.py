import FWCore.ParameterSet.Config as cms

hltSingletRecoPFTau = cms.EDFilter('HLT1PFTau',
  saveTags = cms.bool(True),
  inputTag = cms.InputTag('hltCollection'),
  triggerType = cms.int32(0),
  MinE = cms.double(-1),
  MinPt = cms.double(-1),
  MinMass = cms.double(-1),
  MaxEta = cms.double(-1),
  MinN = cms.int32(1)
)
