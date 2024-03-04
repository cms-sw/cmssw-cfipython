import FWCore.ParameterSet.Config as cms

def DT4DSegmentClients(**kwargs):
  mod = cms.EDProducer('DT4DSegmentClients',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
