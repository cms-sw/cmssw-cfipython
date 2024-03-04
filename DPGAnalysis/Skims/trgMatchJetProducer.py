import FWCore.ParameterSet.Config as cms

def trgMatchJetProducer(**kwargs):
  mod = cms.EDProducer('trgMatchJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
