import FWCore.ParameterSet.Config as cms

def CandMultiplicityCounter(*args, **kwargs):
  mod = cms.EDProducer('CandMultiplicityCounter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
