import FWCore.ParameterSet.Config as cms

def DTBlockedROChannelsTest(**kwargs):
  mod = cms.EDProducer('DTBlockedROChannelsTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
