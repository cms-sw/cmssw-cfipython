import FWCore.ParameterSet.Config as cms

def CandMultiplicityCounter(**kwargs):
  mod = cms.EDProducer('CandMultiplicityCounter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
