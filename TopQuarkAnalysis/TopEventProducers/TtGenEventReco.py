import FWCore.ParameterSet.Config as cms

def TtGenEventReco(**kwargs):
  mod = cms.EDProducer('TtGenEventReco',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
