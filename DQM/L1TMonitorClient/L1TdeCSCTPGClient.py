import FWCore.ParameterSet.Config as cms

def L1TdeCSCTPGClient(**kwargs):
  mod = cms.EDProducer('L1TdeCSCTPGClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
