import FWCore.ParameterSet.Config as cms

def CandViewShallowCloneCombiner(**kwargs):
  mod = cms.EDProducer('CandViewShallowCloneCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
