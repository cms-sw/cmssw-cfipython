import FWCore.ParameterSet.Config as cms

def L1TdeGEMTPGClient(**kwargs):
  mod = cms.EDProducer('L1TdeGEMTPGClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
