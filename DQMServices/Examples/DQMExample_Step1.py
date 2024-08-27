import FWCore.ParameterSet.Config as cms

def DQMExample_Step1(**kwargs):
  mod = cms.EDProducer('DQMExample_Step1',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
