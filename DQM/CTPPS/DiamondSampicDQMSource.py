import FWCore.ParameterSet.Config as cms

def DiamondSampicDQMSource(**kwargs):
  mod = cms.EDProducer('DiamondSampicDQMSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
