import FWCore.ParameterSet.Config as cms

def EwkMuDQM(**kwargs):
  mod = cms.EDProducer('EwkMuDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
