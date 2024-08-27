import FWCore.ParameterSet.Config as cms

def EventAuxiliaryHistoryProducer(**kwargs):
  mod = cms.EDProducer('EventAuxiliaryHistoryProducer',
    historyDepth = cms.required.uint32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
