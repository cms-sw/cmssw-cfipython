import FWCore.ParameterSet.Config as cms

def HLTGenValClient(**kwargs):
  mod = cms.EDProducer('HLTGenValClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
