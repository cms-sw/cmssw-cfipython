import FWCore.ParameterSet.Config as cms

hltGlobalSumsRecoPFMET = cms.EDFilter('HLTGlobalSumsPFMET',
  saveTags = cms.bool(True),
  inputTag = cms.InputTag('hltCollection'),
  triggerType = cms.int32(0),
  observable = cms.string(''),
  Min = cms.double(-1e+125),
  Max = cms.double(1e+125),
  MinN = cms.int32(1)
)
