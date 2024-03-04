import FWCore.ParameterSet.Config as cms

def NeutronHitsCollector(**kwargs):
  mod = cms.EDProducer('NeutronHitsCollector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
