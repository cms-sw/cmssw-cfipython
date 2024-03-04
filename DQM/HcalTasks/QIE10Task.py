import FWCore.ParameterSet.Config as cms

def QIE10Task(**kwargs):
  mod = cms.EDProducer('QIE10Task',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
