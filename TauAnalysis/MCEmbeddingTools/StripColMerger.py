import FWCore.ParameterSet.Config as cms

def StripColMerger(**kwargs):
  mod = cms.EDProducer('StripColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
