import FWCore.ParameterSet.Config as cms

def BasicToPFJet(*args, **kwargs):
  mod = cms.EDProducer('BasicToPFJet',
    src = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
