import FWCore.ParameterSet.Config as cms

def B2GHadronicHLTValidation(**kwargs):
  mod = cms.EDProducer('B2GHadronicHLTValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
