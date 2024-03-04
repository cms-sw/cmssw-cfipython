import FWCore.ParameterSet.Config as cms

def HGCalRecHitsClient(**kwargs):
  mod = cms.EDProducer('HGCalRecHitsClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
