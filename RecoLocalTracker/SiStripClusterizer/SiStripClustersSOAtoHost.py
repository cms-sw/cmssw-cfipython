import FWCore.ParameterSet.Config as cms

def SiStripClustersSOAtoHost(*args, **kwargs):
  mod = cms.EDProducer('SiStripClustersSOAtoHost',
    ProductLabel = cms.InputTag('siStripClusterizerFromRawGPU'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
