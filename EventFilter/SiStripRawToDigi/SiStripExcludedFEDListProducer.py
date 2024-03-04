import FWCore.ParameterSet.Config as cms

def SiStripExcludedFEDListProducer(**kwargs):
  mod = cms.EDProducer('SiStripExcludedFEDListProducer',
    ProductLabel = cms.InputTag('rawDataCollector'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
