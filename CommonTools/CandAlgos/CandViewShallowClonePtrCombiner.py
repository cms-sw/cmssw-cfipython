import FWCore.ParameterSet.Config as cms

def CandViewShallowClonePtrCombiner(**kwargs):
  mod = cms.EDProducer('CandViewShallowClonePtrCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
