import FWCore.ParameterSet.Config as cms

def DT4DSegmentClients(*args, **kwargs):
  mod = cms.EDProducer('DT4DSegmentClients',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
