import FWCore.ParameterSet.Config as cms

def UnclusteredBlobProducer(*args, **kwargs):
  mod = cms.EDProducer('UnclusteredBlobProducer',
    candsrc = cms.InputTag('badUnclustered'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
