import FWCore.ParameterSet.Config as cms

def testNuclearInteractions(**kwargs):
  mod = cms.EDProducer('testNuclearInteractions',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
