import FWCore.ParameterSet.Config as cms

def NamedCandViewCombiner(**kwargs):
  mod = cms.EDProducer('NamedCandViewCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
