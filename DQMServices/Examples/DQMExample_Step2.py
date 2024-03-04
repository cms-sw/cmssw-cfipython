import FWCore.ParameterSet.Config as cms

def DQMExample_Step2(**kwargs):
  mod = cms.EDProducer('DQMExample_Step2',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
