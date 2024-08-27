import FWCore.ParameterSet.Config as cms

def MCMatcherByPt(**kwargs):
  mod = cms.EDProducer('MCMatcherByPt',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
