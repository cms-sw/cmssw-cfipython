import FWCore.ParameterSet.Config as cms

hltHcalNZSFilter = cms.EDFilter('HLTHcalNZSFilter',
  saveTags = cms.bool(False),
  InputTag = cms.InputTag('source')
)
