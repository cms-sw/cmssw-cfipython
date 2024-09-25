import FWCore.ParameterSet.Config as cms

def GeneratorSmearedProducer(*args, **kwargs):
  mod = cms.EDProducer('GeneratorSmearedProducer',
    currentTag = cms.untracked.InputTag('VtxSmeared'),
    previousTag = cms.untracked.InputTag('generator'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
