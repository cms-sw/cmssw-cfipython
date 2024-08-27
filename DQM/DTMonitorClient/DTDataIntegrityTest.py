import FWCore.ParameterSet.Config as cms

def DTDataIntegrityTest(**kwargs):
  mod = cms.EDProducer('DTDataIntegrityTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
