import FWCore.ParameterSet.Config as cms

def HepMCCopy(**kwargs):
  mod = cms.EDProducer('HepMCCopy',
    src = cms.InputTag('generatorSmeared'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
