import FWCore.ParameterSet.Config as cms

def HLTHcalNZSFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTHcalNZSFilter',
    saveTags = cms.bool(True),
    InputTag = cms.InputTag('source'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
