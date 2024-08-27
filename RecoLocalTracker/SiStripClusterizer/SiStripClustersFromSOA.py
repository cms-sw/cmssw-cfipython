import FWCore.ParameterSet.Config as cms

def SiStripClustersFromSOA(**kwargs):
  mod = cms.EDProducer('SiStripClustersFromSOA',
    ProductLabel = cms.InputTag('siStripClustersSOAtoHost'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
