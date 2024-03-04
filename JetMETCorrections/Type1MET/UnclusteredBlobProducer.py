import FWCore.ParameterSet.Config as cms

def UnclusteredBlobProducer(**kwargs):
  mod = cms.EDProducer('UnclusteredBlobProducer',
    candsrc = cms.InputTag('badUnclustered'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
