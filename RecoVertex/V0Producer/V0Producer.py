import FWCore.ParameterSet.Config as cms

def V0Producer(**kwargs):
  mod = cms.EDProducer('V0Producer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
