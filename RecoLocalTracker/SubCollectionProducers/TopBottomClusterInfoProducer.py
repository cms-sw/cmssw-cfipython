import FWCore.ParameterSet.Config as cms

def TopBottomClusterInfoProducer(**kwargs):
  mod = cms.EDProducer('TopBottomClusterInfoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
