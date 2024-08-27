import FWCore.ParameterSet.Config as cms

def BasicToPFJet(**kwargs):
  mod = cms.EDProducer('BasicToPFJet',
    src = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
