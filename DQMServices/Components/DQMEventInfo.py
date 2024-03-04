import FWCore.ParameterSet.Config as cms

def DQMEventInfo(**kwargs):
  mod = cms.EDProducer('DQMEventInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
