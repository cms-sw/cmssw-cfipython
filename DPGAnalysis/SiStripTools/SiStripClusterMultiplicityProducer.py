import FWCore.ParameterSet.Config as cms

def SiStripClusterMultiplicityProducer(**kwargs):
  mod = cms.EDProducer('SiStripClusterMultiplicityProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
