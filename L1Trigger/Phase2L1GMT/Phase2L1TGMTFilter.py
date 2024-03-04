import FWCore.ParameterSet.Config as cms

def Phase2L1TGMTFilter(**kwargs):
  mod = cms.EDProducer('Phase2L1TGMTFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
