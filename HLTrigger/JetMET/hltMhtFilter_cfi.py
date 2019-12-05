import FWCore.ParameterSet.Config as cms

hltMhtFilter = cms.EDFilter('HLTMhtFilter',
  inputMhtTag = cms.InputTag('hltMht30'),
  saveTags = cms.bool(False),
  minMht = cms.double(0)
)
