import FWCore.ParameterSet.Config as cms

def DT2DSegmentClients(**kwargs):
  mod = cms.EDProducer('DT2DSegmentClients',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
