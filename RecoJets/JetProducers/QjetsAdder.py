import FWCore.ParameterSet.Config as cms

def QjetsAdder(**kwargs):
  mod = cms.EDProducer('QjetsAdder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
