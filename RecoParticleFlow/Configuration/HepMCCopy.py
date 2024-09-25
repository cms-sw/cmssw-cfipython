import FWCore.ParameterSet.Config as cms

def HepMCCopy(*args, **kwargs):
  mod = cms.EDProducer('HepMCCopy',
    src = cms.InputTag('generatorSmeared'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
