import FWCore.ParameterSet.Config as cms

def EwkDQM(**kwargs):
  mod = cms.EDProducer('EwkDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
