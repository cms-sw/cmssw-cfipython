import FWCore.ParameterSet.Config as cms

hltHcalNZSFilter = cms.EDFilter('HLTHcalNZSFilter',
  saveTags = cms.bool(True),
  InputTag = cms.InputTag('source')
)
