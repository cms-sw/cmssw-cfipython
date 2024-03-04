import FWCore.ParameterSet.Config as cms

def HLTHcalNZSFilter(**kwargs):
  mod = cms.EDFilter('HLTHcalNZSFilter',
    saveTags = cms.bool(True),
    InputTag = cms.InputTag('source'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
