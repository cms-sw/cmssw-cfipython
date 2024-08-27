import FWCore.ParameterSet.Config as cms

def FSQDQM(**kwargs):
  mod = cms.EDProducer('FSQDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
