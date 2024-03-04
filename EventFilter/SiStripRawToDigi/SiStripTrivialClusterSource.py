import FWCore.ParameterSet.Config as cms

def SiStripTrivialClusterSource(**kwargs):
  mod = cms.EDProducer('SiStripTrivialClusterSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
