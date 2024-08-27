import FWCore.ParameterSet.Config as cms

def ProtonTaggerFilter(**kwargs):
  mod = cms.EDFilter('ProtonTaggerFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
