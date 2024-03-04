import FWCore.ParameterSet.Config as cms

def GeneratorSmearedProducer(**kwargs):
  mod = cms.EDProducer('GeneratorSmearedProducer',
    currentTag = cms.untracked.InputTag('VtxSmeared'),
    previousTag = cms.untracked.InputTag('generator'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
