import FWCore.ParameterSet.Config as cms

def EventAuxiliaryHistoryProducer(*args, **kwargs):
  mod = cms.EDProducer('EventAuxiliaryHistoryProducer',
    historyDepth = cms.required.uint32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
