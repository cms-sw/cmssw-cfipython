import FWCore.ParameterSet.Config as cms

def L1TCaloSummary_CICADA_v1p0p0(**kwargs):
  mod = cms.EDProducer('L1TCaloSummary_CICADA_v1p0p0',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
