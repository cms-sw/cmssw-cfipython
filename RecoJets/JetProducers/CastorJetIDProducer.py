import FWCore.ParameterSet.Config as cms

def CastorJetIDProducer(**kwargs):
  mod = cms.EDProducer('CastorJetIDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
