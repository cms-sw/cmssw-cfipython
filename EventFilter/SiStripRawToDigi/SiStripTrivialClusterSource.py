import FWCore.ParameterSet.Config as cms

def SiStripTrivialClusterSource(*args, **kwargs):
  mod = cms.EDProducer('SiStripTrivialClusterSource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
