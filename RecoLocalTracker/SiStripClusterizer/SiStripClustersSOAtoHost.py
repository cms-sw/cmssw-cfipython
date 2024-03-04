import FWCore.ParameterSet.Config as cms

def SiStripClustersSOAtoHost(**kwargs):
  mod = cms.EDProducer('SiStripClustersSOAtoHost',
    ProductLabel = cms.InputTag('siStripClusterizerFromRawGPU'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
