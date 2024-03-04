import FWCore.ParameterSet.Config as cms

def DQMGenericClient(**kwargs):
  mod = cms.EDProducer('DQMGenericClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
