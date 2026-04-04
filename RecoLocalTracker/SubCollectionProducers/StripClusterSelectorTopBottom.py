import FWCore.ParameterSet.Config as cms

def StripClusterSelectorTopBottom(*args, **kwargs):
  mod = cms.EDProducer('StripClusterSelectorTopBottom',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
