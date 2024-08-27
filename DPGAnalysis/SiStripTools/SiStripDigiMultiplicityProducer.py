import FWCore.ParameterSet.Config as cms

def SiStripDigiMultiplicityProducer(**kwargs):
  mod = cms.EDProducer('SiStripDigiMultiplicityProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
