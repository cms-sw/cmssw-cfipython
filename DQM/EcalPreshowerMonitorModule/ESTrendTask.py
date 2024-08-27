import FWCore.ParameterSet.Config as cms

def ESTrendTask(**kwargs):
  mod = cms.EDProducer('ESTrendTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
