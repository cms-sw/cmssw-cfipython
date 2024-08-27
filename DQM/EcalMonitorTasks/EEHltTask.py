import FWCore.ParameterSet.Config as cms

def EEHltTask(**kwargs):
  mod = cms.EDProducer('EEHltTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
