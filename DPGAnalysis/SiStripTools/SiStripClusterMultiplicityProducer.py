import FWCore.ParameterSet.Config as cms

def SiStripClusterMultiplicityProducer(*args, **kwargs):
  mod = cms.EDProducer('SiStripClusterMultiplicityProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
