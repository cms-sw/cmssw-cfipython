import FWCore.ParameterSet.Config as cms

def StGenEventReco(**kwargs):
  mod = cms.EDProducer('StGenEventReco',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
