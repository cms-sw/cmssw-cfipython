import FWCore.ParameterSet.Config as cms

def CandViewCombiner(**kwargs):
  mod = cms.EDProducer('CandViewCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
