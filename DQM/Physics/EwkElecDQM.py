import FWCore.ParameterSet.Config as cms

def EwkElecDQM(**kwargs):
  mod = cms.EDProducer('EwkElecDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
