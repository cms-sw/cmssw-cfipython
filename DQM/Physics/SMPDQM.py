import FWCore.ParameterSet.Config as cms

def SMPDQM(**kwargs):
  mod = cms.EDProducer('SMPDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
