import FWCore.ParameterSet.Config as cms

def DTSpyReader(**kwargs):
  mod = cms.EDProducer('DTSpyReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
